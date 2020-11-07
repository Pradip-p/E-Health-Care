from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from doctor.models import DoctorInfo

def save_doctorinfo(sender,instance,created,**kwarg):
    if created:
        DoctorInfo.objects.create(user=instance,name=instance.username)