from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name='contact'),
    path('404', views._404, name='_404'),
    path('500', views._500, name='_500'),
]