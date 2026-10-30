
from django import forms
from myapp.models import Student

# class StudentForm(forms.Form):  
#     name=forms.CharField()
#     age=forms.IntegerField()
#     place=forms.CharField()
#     email=forms.EmailField()
#     dob=forms.DateField()



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
