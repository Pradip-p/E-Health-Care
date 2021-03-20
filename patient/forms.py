from django import forms
from django.contrib.auth.models import User
from patient.models import Profile,Feedback
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
		model=Profile
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
	def __init__(self,*args,**kwargs):
		super(ProfileForm,self).__init__(*args,**kwargs)

		self.fields['name'].error_messages.update({'required':'Name can hold atmost 20 characters'})
		self.fields['phone_number'].error_messages.update({'required':'Phone number must be entered in the format +999999999 Up to 15 digits allowed.'})
		self.fields['address'].error_messages.update({'required':'Address can have maximum 40 characters'})	
		self.fields['gender'].error_messages.update({'required':'Please select a gender'})
		self.fields['age'].error_messages.update({'required':'Age must be an integer'})
		self.fields['status'].error_messages.update({'required':'Please select an status'})
		self.fields['profile_pic'].error_messages.update({'required':'Please upload a profile picture'})

class UpdateForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('email',)	
	
	def __init__(self,*args,**kwargs):
		super(UpdateForm,self).__init__(*args,**kwargs)

		self.fields['email'].error_messages.update({'required':'Please enter valid  email'})
		
class FeedbackForm(forms.ModelForm):

	class Meta:
		model=Feedback
		fields=('title','text','picture')
		label={
			'title':'Title',
			'text':'Description',
			'picture':'Picture'
		}
	def __init__(self,*args,**kwargs):
		super(FeedbackForm,self).__init__(*args,**kwargs)

		self.fields['title'].error_messages.update({'required':'Title can hold atmost 50 characters'})
		self.fields['picture'].error_messages.update({'required':'Please upload a picture'})
		self.fields['text'].error_messages.update({'required':'Description should only be 200 characters long'})
