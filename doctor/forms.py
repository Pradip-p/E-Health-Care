from django import forms
from doctor.models import DoctorInfo

class DoctorInfoForm(forms.ModelForm):
    class Meta():
        model = DoctorInfo
        fields = ('username','password')

    
