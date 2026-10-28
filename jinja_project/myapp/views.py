from django.shortcuts import render

# Create your views here.

def view1(request):
    name="rama"
    age=22
    place="banglore"
    ctx={'NAME':name,'AGE':age,'PLACE':place}
    return render(request,'myapp/jinja.html',ctx)

