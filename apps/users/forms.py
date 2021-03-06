from django.contrib.auth.models import User
from django.contrib.auth.forms import forms, UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    email = forms.EmailInput()

    class Meta:
        model = Profile
        fields = ['user_image', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
