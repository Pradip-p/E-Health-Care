from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import CASCADE
from django.contrib.auth.models import User
#from patient.models import PatientInfo
from django.db.models.signals import post_save
from django.db.models import signals
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

    def __str__(self):
        return self.name

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance,name=instance.username)


@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()

# when profile is deleted user is also delete
def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
signals.post_delete.connect(delete_user, sender=Profile)

class Feedback(models.Model):
    text=models.TextField(max_length=200)
    title=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    uploaded_by=models.ForeignKey(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class WhoPredictDisease(models.Model):
    predict_by=models.ForeignKey(Profile,on_delete=models.CASCADE)
    predicted_disease=models.CharField(max_length=30)

    def __str__(self):
        return self.predicted_disease
   

class Disease1(models.Model):
    name=models.CharField(max_length=200)
    doctor=models.ForeignKey(DoctorInfo,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name 

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

class Image(models.Model):
    
    imagefile= models.FileField(upload_to='images/')

class ImageBlock(models.Model):
    imageblock = models.FileField(upload_to='images/')
  
    

