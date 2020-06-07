from django import forms
from django.contrib.auth.models import User
from patient.models import PatientInfo
from django.contrib.auth.forms import UserCreationForm



class PatientInfoForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        # fields='__all__'
        fields = ('username','password')
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']