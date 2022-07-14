from django.urls import path
from . import views

urlpatterns = [
    path('chat-<int:chat_id>', views.chat, name='chat'),
    path('send', views.send, name='send'),
    path('getMessages/chat-<int:chat_id>/', views.getMessages, name='getMessages'),
]