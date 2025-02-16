from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    
class Product_Variant(models.Model):
    sku = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    