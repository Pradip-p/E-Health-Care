from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import CASCADE
from django.contrib.auth.models import User
#from patient.models import PatientInfo
from django.db.models.signals import post_save
from django.dispatch import receiver
from doctor.models import *

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address=models.CharField(max_length=40)
    gender=models.CharField( max_length=50,blank=True,choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    age=models.IntegerField(blank=True , null=True)
    status=models.CharField(max_length=20,blank=True,choices=(('Single','Single'),('Married','Married')))
    profile_pic=models.ImageField(blank=True,null=True)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()
 

class Disease1(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(on_delete= CASCADE, to=DoctorInfo)
    def __str__(self):
        return self.name 



from django.db import models

# Create your models here.
class Heart(models.Model):
    age=models.IntegerField()
    sex=models.IntegerField()
    cp=models.IntegerField()
    trestbps=models.IntegerField()
    chol=models.IntegerField()
    fbs=models.IntegerField()
    restecg=models.IntegerField()
    thalach=models.IntegerField()
    exang=models.IntegerField()
    oldpeak=models.IntegerField()
    slope=models.IntegerField()
    ca	=models.IntegerField()
    thal=models.IntegerField()
    def to_dict(self):
        return{
            'age':self.age,
            'sex':self.sex,
            'cp':self.cp,
            'trestbps':self.trestbps,
            'chol':self.chol,
            'fbs':self.fbs,
            'restecg':self.restecg,
            'thalach':self.thalach,
            'exang':self.exang,
            'slope':self.slope,
            'oldpeak':self.oldpeak,
            'ca':self.ca,
            'thal':self.thal,

        }


class Diabetes(models.Model):
    Pregnancies=models.IntegerField()
    Glucose=models.IntegerField()
    BloodPressure=models.IntegerField()
    SkinThickness=models.IntegerField()
    Insulin=models.IntegerField()
    BMI=models.IntegerField()
    DiabetesPedigreeFunction=models.IntegerField()
    Age=models.IntegerField()
    
    def to_dict(self):
        return{
            'Pregnancies':self.Pregnancies,
            'Glucose':self.Glucose,
            'BloodPressure':self.BloodPressure,
            'SkinThickness':self.SkinThickness,
            'Insulin':self.Insulin,
            'BMI':self.BMI,
            'DiabetesPedigreeFunction':self.DiabetesPedigreeFunction,
            'Age':self.Age,
        }