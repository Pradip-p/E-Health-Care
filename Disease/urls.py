"""Disease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('appointment/', include('appointment.urls')),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('doctor/',include('doctor.urls')),
    path('roleadmin/',include('roleadmin.urls')),
    path('patient/',include('patient.urls')),
    path('health/',include('Health.urls')),
    path('', RedirectView.as_view(url="health/")),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = 'Smart Health'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"
