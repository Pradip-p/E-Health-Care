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


class ProfileForm(forms.ModelForm):
	class Meta:
		model=PatientInfo
		fields=('name','phone_number','address','gender','age','status','profile_pic')
		#exclude=['username','password']
		label={
			
			'phone_number':'Phone Number',
			'address':'Address',
			'gender':'Gender',
			'age':'Age',
			'status':'Status',
			'profile_pic':'Profile Picture'

		}

	
