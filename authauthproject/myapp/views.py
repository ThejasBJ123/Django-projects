
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Registration View
def user_register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        return redirect('login')

    return render(request, 'register.html')


# Login View
def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username and password'
            })

    return render(request, 'login.html')


# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')
