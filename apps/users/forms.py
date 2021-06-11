from django.contrib.auth.models import User
from django.contrib.auth.forms import forms, UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
