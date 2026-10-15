from django.db import models
class Product(models.Model):
    sku=models.CharField(max_length=40,unique=True)
    name=models.CharField(max_length=150)
    category=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    reorder_level=models.PositiveIntegerField(default=10)
class Order(models.Model):
    reference=models.CharField(max_length=40,unique=True)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    customer=models.CharField(max_length=120)
    created_at=models.DateTimeField(auto_now_add=True)
