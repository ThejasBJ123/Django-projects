from django.shortcuts import render

from django.http import HttpResponse

def home2(request):
    return HttpResponse("Hello Everyone! Welcome to secound App.")