from django.urls import path
from . import views

urlpatterns = [
    path('comments:<int:com_id>', views.comments, name='comments'),
]