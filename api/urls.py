from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url
from django.views.generic.base import RedirectView
from rest_framework import routers
from api import views

router=routers.DefaultRouter()

router.register(r'api', views.DiseaseViewSet)
#router.register(r'auth', views.UserViewSet)

urlpatterns=[
    path(r'api/', include(router.urls)),
    path('',RedirectView.as_view(url="api/"))
]