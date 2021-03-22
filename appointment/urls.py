from django.contrib import admin
from django.urls import path,include
from appointment import views
from django.views.generic.base import RedirectView

urlpatterns = [        
path('',RedirectView.as_view(url='appointment/')),
path('appointment/', views.appointment,name='appointment'),
]