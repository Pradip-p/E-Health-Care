from django import forms
from doctor.models import DoctorInfo

class DoctorForm(forms.ModelForm):
    class Meta:
        model=DoctorInfo
        fields='__all__'
        # exclude=('birthday',)

class Trial(forms.ModelForm):
    class Meta:
        model=DoctorInfo
        fields='__all__'