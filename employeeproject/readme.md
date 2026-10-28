.\work\scripts\activate

django-admin startproject employeeproject

cd employeeproject

python manage.py startapp myapp



admin.py
--------

from myapp.models import Product
admin.site.register(Product)

views.py
---------
class Product(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=40)
    dob = models.DateField()
    email_ID = models.EmailField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Product/')




