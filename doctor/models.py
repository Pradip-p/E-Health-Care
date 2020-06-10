from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class DoctorInfo(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    category=models.CharField(max_length=40)

    
    def __str__(self):
        return self.name