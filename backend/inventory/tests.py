from django.test import TestCase,Client
from .models import Product,Order
import json
class InventoryTests(TestCase):
 def setUp(self):self.p=Product.objects.create(sku='T1',name='Demo',category='Tops',price='100.00',stock=5)
 def post(self,d):return self.client.post('/api/orders/',json.dumps(d),content_type='application/json')
 def test_order_decrements_stock_and_snapshots_price(self):
  r=self.post({'product_id':self.p.id,'quantity':2,'customer':'Demo Buyer'});self.assertEqual(r.status_code,201);self.p.refresh_from_db();self.assertEqual(self.p.stock,3);self.assertEqual(r.json()['total'],'200.00')
 def test_overselling_blocked(self):
  self.assertEqual(self.post({'product_id':self.p.id,'quantity':6,'customer':'Buyer'}).status_code,400);self.p.refresh_from_db();self.assertEqual(self.p.stock,5);self.assertEqual(Order.objects.count(),0)
 def test_bad_quantity(self):self.assertEqual(self.post({'product_id':self.p.id,'quantity':0,'customer':'Buyer'}).status_code,400)
 def test_duplicate_sku(self):self.assertEqual(self.client.post('/api/products/',json.dumps({'sku':'T1','name':'Demo','price':10,'stock':1}),content_type='application/json').status_code,400)
 def test_csv_export(self):self.assertContains(self.client.get('/api/export/'),'T1')
 def test_csrf_enforced(self):self.assertEqual(Client(enforce_csrf_checks=True).post('/api/orders/','{}',content_type='application/json').status_code,403)
