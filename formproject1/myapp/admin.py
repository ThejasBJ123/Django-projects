from django.shortcuts import render
from myapp.models import Student

def Student_list(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        place = request.POST['place']
        email = request.POST['email']
        feedback = request.POST['feedback']

        Student.objects.create(
            name=name,
            age=age,
            place=place,
            email=email,
            feedback=feedback
        )

    s = Student.objects.all()

    return render(request, 'home.html', {'stud': s})