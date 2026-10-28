from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=40)
    material=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='Product/')
    
