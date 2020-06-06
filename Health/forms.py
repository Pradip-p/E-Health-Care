from django import forms
from api.models import Disease

class DiseaseForm(forms.ModelForm):
    class Meta():
        model = Disease
        fields='__all__'
    
