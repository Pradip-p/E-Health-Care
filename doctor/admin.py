from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from doctor.models import DoctorInfo
# Register your models here.
class DoctorInfoAdmin(ModelAdmin):
    list_display=['name','phone_number','email','category']
    list_filter=['name','phone_number','category']
    search_fields=['name','phone_number','category']
admin.site.register(DoctorInfo,DoctorInfoAdmin)

