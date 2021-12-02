from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_todos),
    path('todo/',views.todo),
    path('todo/<int:id>/', views.display_single_todo),
    path('display_todos/', views.display_todos, name='display_todos'),
    path('todo/<int:id>/<int:done_clicked>/', views.done_click, name='done_click'),
    path('todo/<str:category>/',views.category_display, name='category_display'),
    path('delete/<int:id>/',views.delete_task),
    path('delete/',views.delete_all)
]