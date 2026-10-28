
from django.shortcuts import render
from myapp.models import Student

def student_list(request):
    s = Student.objects.all()
    d = {'stud': s}
    return render(request, 'student.html', d)
