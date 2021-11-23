from django.urls import path
from . import views

urlpatterns = [
    path('persons/<str:phonenumber>/', views.persons_phonenumber,name='persons_phonenumber'),
    path('persons/<str:name_str>/', views.persons_name, name='persons_name')
]
