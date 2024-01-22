from django.shortcuts import render
from drug_interaction.models import Drug
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