
from django.shortcuts import render


def myview(request):
    name = "thejas"
    age = 22

    return render(request, 'myapp/index.html', {
        'name': name,
        'age': age
    })

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')
