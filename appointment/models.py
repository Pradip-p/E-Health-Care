from django.db import models
from doctor.models import DoctorInfo
from patient.models import *

# Create your models here.


class AppointmentDetails(models.Model):
    day_choice = (
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    )

  

    appointment_day=models.CharField(max_length=20,choices=day_choice)
    appointment_start_time=models.TimeField(auto_now=False,auto_now_add=False)
    appointment_end_time=models.TimeField(auto_now=False,auto_now_add=False)
    appointment_date=models.DateTimeField()
    appointment_status=models.IntegerField(default=0)
    create_by=models.ForeignKey(DoctorInfo,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.appointment_day


class BookedAppointment(models.Model):
    booked_by=models.ForeignKey(Profile,on_delete=models.CASCADE)
    appointment_id=models.OneToOneField(AppointmentDetails,on_delete=models.CASCADE)
    reason=models.TextField(max_length=100)

    def __str__(self):
        return self.reason



