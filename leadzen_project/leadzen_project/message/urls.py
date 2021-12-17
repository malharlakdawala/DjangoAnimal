from django.urls import path
from . import views

# message.urls.py
urlpatterns = [
    path('<str:str>/', views.message, name='message'),
    path('email/<str:mails>', views.email, name='email'),
    path('sms/<str:str>', views.sms, name='sms'),
    path('whatsapp/<str:phn>/<str:name>/', views.whatsapp, name='whatsapp'),
    path('call/<str:phn>/<str:name>/', views.call, name='call'),
]
