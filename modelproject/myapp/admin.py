from django.contrib import admin
from myapp.models import Student
# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display=['name','place','email']
    
admin.site.register(Student, Studentadmin)



