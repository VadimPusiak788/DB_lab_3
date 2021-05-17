from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm


class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '../'
