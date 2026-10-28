from django.shortcuts import render

# Create your views here.
from myapp.models import Student
def Student_list(request): 
    s=Student.objects.all()
    p={'stud':s}
    return render(request,'student.html',p)
