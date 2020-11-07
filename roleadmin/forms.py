from patient.models import Disease1
from doctor.models import DoctorInfo
from django import forms
from django.forms import ModelChoiceField

class AddDiseaseForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(),label='Disease Name')
    doctor=forms.ModelChoiceField(queryset=DoctorInfo.objects.all(),initial=0)

    class Meta:
        model=Disease1
        fields=["name","doctor",]










