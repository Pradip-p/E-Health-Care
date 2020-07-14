from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from doctor.models import DoctorInfo
# Register your models here.

admin.site.register(DoctorInfo)