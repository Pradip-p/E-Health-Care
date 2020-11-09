from django import forms
from doctor.models import DoctorInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorForm(forms.ModelForm):
    class Meta:
        model=DoctorInfo
        exclude=('user',)

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }
