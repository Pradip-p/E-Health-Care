from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import CASCADE
from django.contrib.auth.models import User
#from patient.models import PatientInfo
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address=models.CharField(max_length=40)
    gender=models.CharField( max_length=50,blank=True,choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    age=models.IntegerField(blank=True)
    status=models.CharField(max_length=20,blank=True,choices=(('Single','Single'),('Married','Married')))
    profile_pic=models.ImageField(blank=True,null=True,upload_to='media')

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()
 


class DiseaseCategory(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Disease1(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(on_delete= CASCADE, to=DiseaseCategory)
    def __str__(self):
        return self.name 
class Doctor(models.Model):
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address=models.CharField(max_length=40)
    gender=models.CharField( max_length=50,default='Male',choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    age=models.CharField(default=18, max_length=20)
    category=models.ForeignKey(on_delete=CASCADE, to=Disease1)
