from django.urls import path
from . import views

urlpatterns = [
    path('messages/<str:room_name>/', views.get_messages),
    path('send-message/', views.send_message),
]
