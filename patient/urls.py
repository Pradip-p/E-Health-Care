from django.urls import path
from patient import views
from django.views.generic.base import RedirectView

1
urlpatterns = [   
path('chat/',views.chat,name="chat"),
path('patient/',RedirectView.as_view(url='patient_login/')),
path('patient_login/', views.patient_login,name='patient_login'),
path('patient_register/', views.patient_register,name='patient_register'),
path('patient_profile/',views.patient_profile,name='patient_profile'),
path('my_profile/',views.my_profile,name="my_profile"),
path('search_doctor/', views.search_doctor,name="search_doctor"),
path('search_doctor/doctor_profile/<int:pk>',views.doctor_profile),
path('dashboard/', views.dashboard, name="dashboard"),
path('home/',views.home,name="home"),
path('home/doctor_profile/<int:pk>',views.doctor_profile),
path('feedback/',views.feedback,name="feedback"),
path('feedback/detail/<int:pk>',views.feedback_detail),
path('feedback/edit/<int:pk>',views.feedback_edit),
path('feedback/add_feedback',views.feedback_add),
path('feedback/delete/<int:pk>',views.feedback_delete),
path('view_appointment/',views.view_appointment,name="view_appointment"),
path('patient_appointment/',views.patient_appointment,name="patient_appointment"),
path('view_appointment/take/<int:pk>',views.take_appointment),
path('patient_appointment/cancel/<int:pk>',views.cancel_appointment),
path('patient_appointment/details/<int:pk>',views.details_appointment),
path('patient_appointment/details/<int:pk>/export_pdf',views.export_pdf),
path('logoutpatient/', views.logoutpatient, name="logoutpatient"),
path('heart/', views.heart, name="heart"),
path('diabetes/', views.diabetes, name="diabetes"),
path('showimage/', views.showimage, name="showimage"),
]