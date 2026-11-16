from django.shortcuts import render,redirect
from myapp.models import Product
from myapp.forms import Productform

# Create your views here.

def display(request):
    data = Product.objects.all()
    d={'prod':data}
    return render(request, 'product.html', d)


def createproduct(request):
    f=Productform()
    if request.method=="POST":
        f=Productform(request.POST,request.FILES)  #request.FILES is compalurary
        if f.is_valid():
            f.save()
        return redirect('display')
    d={'form':f}
    return render(request,'insertform.html',d)