import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
import django;django.setup()
from inventory.models import Product
items=[('AP-001','Classic Cotton Shirt','Shirts','799',48),('AP-002','Linen Summer Shirt','Shirts','1299',8),('AP-003','Everyday Denim','Bottoms','1599',32),('AP-004','Relaxed Chino','Bottoms','1199',6),('AP-005','Essential Polo','Tops','699',64),('AP-006','Crew Neck Tee','Tops','449',72),('AP-007','Lightweight Jacket','Outerwear','2299',15),('AP-008','Cotton Kurta','Ethnic','999',22)]
for sku,name,cat,price,stock in items:Product.objects.get_or_create(sku=sku,defaults={'name':name,'category':cat,'price':price,'stock':stock})
print('Seeded fictional demo inventory; existing data preserved')
