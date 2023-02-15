from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserRegisterForm


class AccountRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'


class AccountLoginView(LoginView):
    model = User
    template_name = 'accounts/login.html'


class AccountLogoutView(LogoutView):
    model = User
    template_name = 'accounts/logout.html'
