from django import forms
from myapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_name(self):
        n = self.cleaned_data['name']

        if len(n) <= 3:
            raise forms.ValidationError(
                "Minimum number of characters must be greater than 3"
            )
        
        return n