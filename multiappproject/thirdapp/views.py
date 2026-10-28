from django.shortcuts import render


from django.http import HttpResponse

def home3(request):
    return HttpResponse("Hello Everyone! Welcome to third App.")
