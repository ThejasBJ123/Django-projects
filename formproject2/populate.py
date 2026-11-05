import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'formproject2.settings')
django.setup()
from faker import Faker
from myapp.models import Student
f = Faker('en_IN')
def generate_populate(n):
    for i in range(n):
        fname=f.name()
        fage=f.random_int(min=20,max=50)
        femail=f.email()
        s=Student.objects.get_or_create(name=fname,age=fage,email=femail)
    
generate_populate(20)



