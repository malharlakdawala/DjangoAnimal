from django.urls import path
from . import views


urlpatterns = [
    path('family/<int:id>/', views.family),
    path('animal/<int:id>/', views.animal),
    path('animals/', views.animals)
]
