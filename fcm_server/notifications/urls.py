from django.urls import path
from .views import send_signup_notification

urlpatterns = [
    path('send-signup-notification/', send_signup_notification, name='send_signup_notification'),
]
