from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('chat.urls')),
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
