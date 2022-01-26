from django.urls import path
from . import views

# message.urls.py
urlpatterns = [
    path('<str:str>/', views.message, name='message'),
    path('email/<str:mails>/', views.email, name='email'),
    path('sms/<str:phn>/', views.sms, name='sms'),
    path('whatsapp/<str:phn>/<str:name>/', views.whatsapp, name='whatsapp'),
    path('call/<str:phn>/<str:name>/', views.call, name='call'),
    path('logs/<int:id>/', views.logs, name='logs'),
    path('whatsapp_log/<int:id>', views.whatsapp_log, name='whatsapp_log'),
]
