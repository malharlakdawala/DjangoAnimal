from django.urls import path
from . import views

urlpatterns = [
    path('add_data_customer/<int:id>',views.add_data),
    path('add_rental_data/<int:id>',views.add_rental_data),
    path('rent/rental/',views.all_rental, name='all_rental'),
    path('rent/rental/<int:id>/',views.single_rental, name='single_rental'),
    path('rent/rental/add/',views.add_rental, name='add_rental'),

    path('rent/customer/', views.all_customer, name='all_customer'),
    path('rent/customer/<int:id>/', views.single_rental, name='single_customer'),
    path('rent/customer/add/', views.add_customer, name='add_customer'),

    path('rent/vehicle/', views.all_vehicle, name='all_vehicle'),
    path('rent/vehicle/<int:id>/', views.single_rental, name='single_vehicle'),
    path('rent/vehicle/add/', views.add_vehicle, name='add_vehicle'),

    path('',views.home, name='home')

]
