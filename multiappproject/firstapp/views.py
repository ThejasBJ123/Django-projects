from django.shortcuts import render

from django.http import HttpResponse

def home1(request):
    a="<h1 style='color:red' > <u> Hello Everyone! Welcome to First App."
    return HttpResponse(a)
