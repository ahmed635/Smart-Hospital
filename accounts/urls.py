from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('profile-<int:pat_id>', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('reset-password', views.reset_password, name='reset_password'),
    path('forget-password', views.forget_password, name='forget_password'),
]
