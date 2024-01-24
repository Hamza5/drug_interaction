from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from drug_interaction.models import Drug, ProductName
from .forms import DrugInteractionForm

def check_drug_interactions(request):
    if request.method == 'POST':
        form = DrugInteractionForm(request.POST)
        if form.is_valid():
            drug1_name = form.cleaned_data['drug1_name']
            drug2_name = form.cleaned_data['drug2_name']

            try:
                drug1 = Drug.objects.get(name=drug1_name)
                drug2 = Drug.objects.get(name=drug2_name)

                # Check for drug interactions based on their relationships
                interactions = set(drug1.atc_codes.all()).intersection(set(drug2.atc_codes.all()))
                
                return render(request, 'interactions.html', {'interactions': interactions})
            
            except Drug.DoesNotExist:
                # Handle if drugs are not found
                print("nottttfound")

    else:
        form = DrugInteractionForm()

    return render(request, 'check_interactions.html', {'form': form})


class ProductShowUpdate(UpdateView):
    model = ProductName
    fields = '__all__'
    template_name = 'product.html'
    success_url = reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = ProductName.objects.get(id=self.kwargs['pk'])
        return context


class ProductListCreate(CreateView):
    model = ProductName
    template_name = 'product_list.html'
    fields = '__all__'
    success_url = reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductName.objects.all()
        return context
