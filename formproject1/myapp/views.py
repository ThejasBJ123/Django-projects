from django.shortcuts import render, redirect
from myapp.models import Student
from myapp.forms import StudentForm

def Student_list(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:
        form = StudentForm()
    s = Student.objects.all()
    p = {
        'stud': s,
        'form': form
    }

    return render(request, 'home.html', p)