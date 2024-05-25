from django.urls import path
from django.contrib.auth.views import *
from .views import *

app_name = 'users'


urlpatterns = [
    path('signup/', SignUpView.as_view(template_name = 'users/signup.html'), name = 'signup'),
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
]
