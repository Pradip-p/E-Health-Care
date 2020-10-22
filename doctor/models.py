from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class DoctorInfo(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    birthday=models.DateField()
    # category=models.CharField(max_length=40)
    picture=models.ImageField(blank=True,null=True)
    department=models.CharField(max_length=30)
    gender=models.CharField( max_length=50,blank=True,choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    doc_id=models.CharField(max_length=50,unique=True)
    education_college=models.CharField(max_length=100)
    education_degree=models.CharField(max_length=100)
    education_year=models.CharField(max_length=50)
    def __str__(self):
        return self.name


