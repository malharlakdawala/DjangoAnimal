from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.UserUpdateView.as_view(), name='my_profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('add_data/', views.add_data, name='add_data'),
]
