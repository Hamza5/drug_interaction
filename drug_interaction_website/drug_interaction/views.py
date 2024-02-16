from django.shortcuts import render

from drug_interaction.models import Drug, Interaction


def check_drug_interactions(request):
    drug_names = request.GET.getlist('drugs')
    errors = []
    for drug_name in drug_names:
        if not Drug.objects.filter(name=drug_name).exists():
            errors.append(f'Drug "{drug_name}" does not exist')
    if errors:
        return render(
            request, 'check_interactions.html',
            {
                'errors': errors, 'drugs': drug_names, 'all_drugs': [drug.name for drug in Drug.objects.all()]
            }
        )
    if drug_names:
        interactions = Interaction.objects.filter(drug1__name__in=drug_names, drug2__name__in=drug_names)
    else:
        interactions = None
    return render(
        request,
        'check_interactions.html',
        {
            'interactions': interactions, 'drugs': drug_names, 'all_drugs': [drug.name for drug in Drug.objects.all()]
        }
    )
