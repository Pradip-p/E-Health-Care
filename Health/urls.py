from django.contrib import admin
from django.urls import path,include
from Health import views
from django.views.generic.base import RedirectView

urlpatterns = [        
path('',RedirectView.as_view(url='index/')),
path('index/', views.index,name='index'),
]