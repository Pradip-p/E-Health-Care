from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class DoctorInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    address=models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    picture=models.ImageField(blank=True,null=True)
    department=models.CharField(max_length=30)
    gender=models.CharField( max_length=50,blank=True,choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    doctorID=models.CharField(max_length=50,unique=True)
    education_college=models.CharField(max_length=100)
    education_degree=models.CharField(max_length=100)
    education_year=models.DateTimeField()

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    


