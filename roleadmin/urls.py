from django.urls import path,include
from roleadmin import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('roleadmin_login/',views.roleadmin_login,name="roleadmin_login"),
    path('roleadmin_logout/',views.roleadmin_logout,name="roleadmin_logout"),
    path('doctors_list/',views.doctors_list,name="doctors_list"),
    path('doctors_list/edit/<int:pk>',views.edit_doctor),
    path('patients_list/',views.patients_list,name="patients_list"),
]
