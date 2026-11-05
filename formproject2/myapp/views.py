from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import StudentForm
from myapp.models import Student


def form_view(request):
    f = StudentForm()

    if request.method == 'POST':
        f = StudentForm(request.POST)

        if f.is_valid():
            f = f.save()
            s = Student.objects.all()
            d = {'stud': s}

            return render(request, '1.html', d)

    d = {'form': f}
    return render(request, 'form.html', d)