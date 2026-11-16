
work\scripts\activate
python -m django startproject productprojects

cd productprojects

py manage.py startapp myapp

## settings file  --> myapp

## models 

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.IntegerField()
    img = models.ImageField(upload_to='products/')


admin page
from myapp.models import Product


admin.site.register(Product)


SETTINGS 

URLS


python manage.py makemigrations 
python manage.py migrate


python manage.py createsuperuser

