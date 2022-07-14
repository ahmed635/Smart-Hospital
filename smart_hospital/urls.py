from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path as url
import notifications.urls

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('patient/', include('patient.urls')),
    path('workstation_nurse/', include('workstation_nurse.urls')),
    path('medication_nurse/', include('medication_nurse.urls')),
    path('doctor/', include('doctor.urls')),
    path('manager/', include('manager.urls')),
    path('comments/', include('comments.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('chatapp/', include('chatapp.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
