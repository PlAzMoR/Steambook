from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('posts:index')
    # template_name = 'users/signup.html'
