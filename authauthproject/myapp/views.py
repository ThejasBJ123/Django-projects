from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("logged in successful")
        else:
            return render(request,'login.html',
                          {'error':'invalid username and password'})
    return render(request,'login.html')

@ login_required
def dashboard(request):
    return render(request,'dashboard.html')


