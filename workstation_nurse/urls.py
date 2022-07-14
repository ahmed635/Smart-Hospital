from django.urls import path
from . import views

urlpatterns = [
    path('', views.workstation_nurse, name= 'workstation_nurse'),
    path('getRealParameters', views.getRealParameters, name='getRealParameters'),

]