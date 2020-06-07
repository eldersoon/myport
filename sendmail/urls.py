from django.urls import path

from .views import sendmail

urlpatterns = [
    path('send/mail', sendmail, name='sendmail'),
]
