from django import forms

class DrugInteractionForm(forms.Form):
    drug1_name = forms.CharField(max_length=255)
    drug2_name = forms.CharField(max_length=255)