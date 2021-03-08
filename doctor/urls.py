from django.contrib import admin
from django.urls import path,include
from doctor import views
from django.views.generic.base import RedirectView

urlpatterns = [        
#path('doctor/',RedirectView.as_view(url='doctor_login/')),
path('doctor_login/', views.doctor_login,name='doctor_login'),
# path('doctor_register/', views.doctor_register,name='doctor_register'),

path('dashboard_doctor/', views.dashboard_doctor, name="dashboard_doctor"),
path('doctor_logout/', views.doctor_logout, name="doctor_logout"),

]