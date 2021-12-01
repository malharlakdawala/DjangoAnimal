from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_todos),
    path('todo/',views.todo),
    path('todo/<int:id>/', views.display_single_todo)
]