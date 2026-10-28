from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=40)
    dob = models.DateField()
    email_ID = models.EmailField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Product/')
    
    
    