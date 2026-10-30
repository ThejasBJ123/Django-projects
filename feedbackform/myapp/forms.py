# class studnetform(forms.Form):
#     name=forms.forms.CharField()
#     age=forms.IntergerField()
#     email=forms.forms.EmailField(, required=False)
#     feedback=forms.CharField()
    
    
from django import forms
from myapp.models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'