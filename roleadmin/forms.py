from patient.models import Disease1
from doctor.models import DoctorInfo
from django import forms

class AddDiseaseForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(),label='Disease Name',error_messages={'required':'Enter upto 200 characters'})
    doctor=forms.ModelChoiceField(queryset=DoctorInfo.objects.all(),initial=0,error_messages={'required':'Please select a doctor'})

    class Meta:
        model=Disease1
        fields=["name","doctor",]

    def __init__(self,*args,**kwargs):
        super(AddDiseaseForm,self).__init__(*args,**kwargs)
        self.fields['name'].error_messages.update({'required':'Enter upto 200 characters'})
        self.fields['doctor'].error_messages.update({'required':'Please select a doctor'})
