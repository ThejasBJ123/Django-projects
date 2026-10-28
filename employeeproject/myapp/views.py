from django.shortcuts import render

# Create your views here.

from myapp.models import Product
def product_list(request): 
    p=Product.objects.all()
    d={'prod':p}
    return render(request,'home.html',d)







