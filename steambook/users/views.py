from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class CustomLoginView(LoginView):
    authentification_form = LoginForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('posts:index')
