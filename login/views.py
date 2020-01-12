from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'login/home.html')


def sign_up(request):
    return render(request, 'login/signup.html')
