from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import StudentForm


def form_view(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponse("Response Recorded")

    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form})