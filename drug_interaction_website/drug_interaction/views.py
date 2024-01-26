from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.core.paginator import Paginator

from drug_interaction.models import Drug, ProductName, ATCCode


def check_drug_interactions(request):
    drug_names = request.GET.getlist('drugs')
    errors = []
    for drug_name in drug_names:
        if not Drug.objects.filter(name=drug_name).exists():
            errors.append(f'Drug "{drug_name}" does not exist')
    if errors:
        return render(request, 'check_interactions.html', {'errors': errors, 'drugs': drug_names})
    if drug_names:
        interactions = {}
        drugs = Drug.objects.filter(name__in=drug_names)
        for drug1 in drugs:
            for drug2 in drugs:
                if drug1 != drug2 and (drug2.name, drug1.name) not in interactions.keys():
                    if drug1_drug2_atc_codes := drug1.atc_codes.all().intersection(drug2.atc_codes.all()):
                        interactions[(drug1.name, drug2.name)] = drug1_drug2_atc_codes
    else:
        interactions = None
    return render(request, 'check_interactions.html', {'interactions': interactions, 'drugs': drug_names})


class ProductShowUpdate(UpdateView):
    model = ProductName
    fields = '__all__'
    template_name = 'product.html'
    success_url = reverse_lazy('products')


class ProductListCreate(CreateView):
    model = ProductName
    template_name = 'product_list.html'
    fields = '__all__'
    success_url = reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = ProductName.objects.all().order_by('name')
        paginator = Paginator(products, self.request.GET.get('page_size', 25))
        page = self.request.GET.get('page', 1)
        context['products'] = paginator.get_page(page)
        return context


class ATCCodeListCreate(CreateView):
    model = ProductName
    template_name = 'atc_code_list.html'
    fields = '__all__'
    success_url = reverse_lazy('atc_codes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        atc_codes = ATCCode.objects.all().order_by('code')
        paginator = Paginator(atc_codes, self.request.GET.get('page_size', 25))
        page = self.request.GET.get('page', 1)
        context['atc_codes'] = paginator.get_page(page)
        return context


class ATCCodeShowUpdate(UpdateView):
    model = ATCCode
    fields = '__all__'
    template_name = 'atc_code.html'
    success_url = reverse_lazy('atc_codes')


class DrugListCreate(CreateView):
    model = Drug
    fields = '__all__'
    template_name = 'drug_list.html'
    success_url = reverse_lazy('drugs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drugs = Drug.objects.all().order_by('name')
        paginator = Paginator(drugs, self.request.GET.get('page_size', 25))
        page = self.request.GET.get('page', 1)
        context['drugs'] = paginator.get_page(page)
        return context


class DrugShowUpdate(UpdateView):
    model = Drug
    fields = '__all__'
    template_name = 'drug.html'
    success_url = reverse_lazy('drugs')
