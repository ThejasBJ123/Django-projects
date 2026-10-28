from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def views1(request):
    a = "Welcome to Django session"
    return HttpResponse(a)


def views2(request):
    b="hello Everone "
    return HttpResponse(b)