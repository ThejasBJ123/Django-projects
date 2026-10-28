from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def add(request):
    a=int(input("Enter a n1: "))
    b=int(input("Enter a n2: "))
    c=a+b
    d=a+b
    return HttpResponse(str(c))


