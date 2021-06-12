from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserEditForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class UserLogInView(LoginView):
    template_name = 'users/login.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserEditForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('home_page:home-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ProfileView, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


class PasswordEditView(PasswordChangeView):
    template_name = 'users/password_edit.html'
    success_url = reverse_lazy('login')
