from django import forms
from doctor.models import DoctorInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorForm(forms.ModelForm):
    class Meta:
        model=DoctorInfo
        exclude=('user',)
    def __init__(self,*args,**kwargs):
        super(DoctorForm,self).__init__(*args,**kwargs)
        self.fields['phone_number'].error_messages.update({'required':'Phone number must be entered in the format +999999999 Up to 15 digits allowed.'})
        self.fields['address'].error_messages.update({'required':'Address can hold max length of 100 characters'})
        self.fields['picture'].error_messages.update({'required':'Uploading a picture is optional'})
        self.fields['department'].error_messages.update({'required':'Department can hold max length of 100 characters'})
        self.fields['gender'].error_messages.update({'required':'This is optional'})
        self.fields['doctorID'].error_messages.update({'required':'Doctor ID field must be unique'})
        self.fields['education_college'].error_messages.update({'required':' Can hold max length of 100 characters'})
        self.fields['education_degree'].error_messages.update({'required':' Can hold max length of 100 characters'})
        self.fields['education_year'].error_messages.update({'required':'This must be an integer'})

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.TextInput()
        }
