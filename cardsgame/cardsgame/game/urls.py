from django.urls import path
from . import views


urlpatterns = [
    path('my_cards', views.my_cards, name='my_cards'),
    path('transfer/<int:id>', views.transfer, name='transfer'),
    path('homepage', views.homepage, name='homepage'),
]