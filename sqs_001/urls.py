# sqs_integration/urls.py

from django.contrib import admin
from django.urls import path
from app.views import send_message_to_sqs,retrive_mesage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_message/', send_message_to_sqs, name='send_message_to_sqs'),
    
    path('r/', retrive_mesage, name='retrive_mesage'),
    
]
