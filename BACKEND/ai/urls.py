from django.urls import path
from . import views

app_name = 'ai'

urlpatterns =[
    path('test/', views.test),
    path('send/alert/', views.send_alert),
]