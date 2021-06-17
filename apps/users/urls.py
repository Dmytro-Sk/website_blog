from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLogInView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password/', views.PasswordEditView.as_view(), name='password-edit'),
]
