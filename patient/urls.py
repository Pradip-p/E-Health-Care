from django.contrib import admin
from django.urls import path,include
from patient import views
from django.views.generic.base import RedirectView

urlpatterns = [        
path('patient/',RedirectView.as_view(url='patient_login/')),
path('patient_login/', views.patient_login,name='patient_login'),
path('patient_register/', views.patient_register,name='patient_register'),
path('patient_profile/',views.patient_profile,name='patient_profile'),
path('my_profile/',views.my_profile,name="my_profile"),

path('form/', views.form, name="form"),

path('search_doctor/', views.search_doctor,name="search_doctor"),
path('search_doctor/doctor_profile/<int:pk>',views.doctor_profile),
#path('update_profile/',views.patient_update,name='update_profile'),
path('dashboard/', views.dashboard, name="dashboard"),

path('home/',views.home,name="home"),
path('home/doctor_profile/<int:pk>',views.doctor_profile),
path('feedback/',views.feedback,name="feedback"),
path('feedback/detail/<int:pk>',views.feedback_detail),
path('feedback/edit/<int:pk>',views.feedback_edit),
path('feedback/add_feedback',views.feedback_add),
path('feedback/delete/<int:pk>',views.feedback_delete),

# path('check/', views.check, name="check"),
path('logoutpatient/', views.logoutpatient, name="logoutpatient"),

path('heart/', views.heart, name="heart"),
path('diabetes/', views.diabetes, name="diabetes"),

path('showimage/', views.showimage, name="showimage"),

]