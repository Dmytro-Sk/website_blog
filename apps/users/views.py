from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
