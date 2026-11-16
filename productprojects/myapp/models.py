from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.IntegerField()
    img = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name