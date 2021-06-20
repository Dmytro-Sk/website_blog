from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from .models import Profile
from .serializer import ProfileSerializer


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class UserLogInView(LoginView):
    template_name = 'users/login.html'


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile_edit.html', context)


class PasswordEditView(PasswordChangeView):
    template_name = 'users/password_edit.html'
    success_url = reverse_lazy('login')


class ProfileAPIView(APIView):
    def get(self, request):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer(queryset, many=True)
        return Response(serializer_class.data)
