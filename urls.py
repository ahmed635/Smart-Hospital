from django.urls import path
from . import views

urlpatterns = [
    path('', views.medication_nurse, name='medication_nurse'),
    path('add-vital-<int:vital_id>', views.vital, name='vital'),
    path('add-medication-<int:med_id>', views.medications, name='medications'),
    path('done', views.done, name='done'),
]