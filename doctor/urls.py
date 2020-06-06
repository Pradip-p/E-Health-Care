from django.contrib import admin
from django.urls import path,include
from doctor import views
from django.views.generic.base import RedirectView

urlpatterns = [        
path('doctor/',RedirectView.as_view(url='doctor_login/')),
path('doctor_login/', views.doctor_login,name='doctor_login'),
]