from django.contrib import admin
from appointment.models import AppointmentDetails,BookedAppointment
# Register your models here.
admin.site.register(AppointmentDetails)
admin.site.register(BookedAppointment)