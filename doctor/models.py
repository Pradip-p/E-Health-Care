from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class DoctorInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # name=models.CharField(max_length=200)
    # username=models.CharField(max_length=40)
    # password=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    # email=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # age=models.IntegerField()
    # hospital=models.CharField(max_length=100)
    # category=models.CharField(max_length=40)
    picture=models.ImageField(blank=True,null=True)
    department=models.CharField(max_length=30)
    gender=models.CharField( max_length=50,blank=True,choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    doctorID=models.CharField(max_length=50,unique=True)
    education_college=models.CharField(max_length=100)
    education_degree=models.CharField(max_length=100)
    education_year=models.CharField(max_length=50)


    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name+""+self.user.last_name

    # def __str__(self):
    #     return self.name

# @receiver(post_save,sender=User)
# def create_user_profile(sender,instance,created,**kwargs):
# 	if created:
# 		DoctorInfo.objects.create(user=instance,name=instance.username)

# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,**kwargs):
# 	instance.doctorinfo.save()

# # when profile is deleted user is also delete
# def delete_user(sender, instance=None, **kwargs):
#     try:
#         instance.user
#     except User.DoesNotExist:
#         pass
#     else:
#         instance.user.delete()
# signals.post_delete.connect(delete_user, sender=DoctorInfo)
