from django.urls import path
from . import views

urlpatterns = [
    path('patient-<int:pat_id>', views.patient, name='patient'),
    path('chart-<int:chart_id>', views.charts, name='charts'),
    
]