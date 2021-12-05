from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', LoginView.as_view(template_name='mainpage/login.html',success_url = reverse_lazy('homepage')), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.UserUpdateView.as_view(), name='my_profile'),
    path('signup/', views.SignupView.as_view(), name='signup'),

]
