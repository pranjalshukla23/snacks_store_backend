from django.db import models

# Create your models here.

# Product
class Product(models.Model):
    product_code = models.CharField(max_length=5, unique=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product_code} - {self.product_name}"
    
# Cart
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"
    
    
    