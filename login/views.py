from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('home')
    else:
        return render(request, 'login/home.html')


def sign_up(request):
    return render(request, 'login/signup.html')
