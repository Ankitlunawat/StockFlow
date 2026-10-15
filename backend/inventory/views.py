import csv,json,uuid
from decimal import Decimal, InvalidOperation
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.db.models import F
from .models import Product,Order
from pathlib import Path

@ensure_csrf_cookie
def index(request):
    return HttpResponse((Path(__file__).resolve().parents[2]/'frontend/dist/index.html').read_text())
def error(message):return JsonResponse({'error':message},status=400)
def product_dict(p):return {'id':p.id,'sku':p.sku,'name':p.name,'category':p.category,'price':str(p.price),'stock':p.stock,'reorder_level':p.reorder_level}
def order_dict(o):return {'reference':o.reference,'customer':o.customer,'product':o.product.name,'quantity':o.quantity,'total':str(o.quantity*o.unit_price)}
@require_http_methods(['GET','POST'])
def products(request):
    if request.method=='GET':return JsonResponse({'products':[product_dict(p) for p in Product.objects.order_by('sku')]})
    try:
        d=json.loads(request.body);price=Decimal(str(d['price']));stock=int(d['stock'])
        if price<=0 or stock<0 or not d['name'].strip() or not d['sku'].strip():return error('Name, unique SKU, positive price and nonnegative stock required')
        if Product.objects.filter(sku=d['sku']).exists():return error('SKU already exists')
        p=Product.objects.create(sku=d['sku'][:40],name=d['name'][:150],category=d.get('category','General')[:60],price=price,stock=stock)
        return JsonResponse(product_dict(p),status=201)
    except (KeyError,ValueError,InvalidOperation,TypeError):return error('Invalid product data')
@require_http_methods(['GET','POST'])
def orders(request):
    if request.method=='GET':return JsonResponse({'orders':[order_dict(o) for o in Order.objects.select_related('product').order_by('-id')]})
    try:
        d=json.loads(request.body);qty=int(d['quantity']);customer=d['customer'].strip()
        if qty<=0 or not customer:return error('Customer and positive quantity required')
        with transaction.atomic():
            p=Product.objects.get(pk=d['product_id'])
            changed=Product.objects.filter(pk=p.pk,stock__gte=qty).update(stock=F('stock')-qty)
            if not changed:return error('Insufficient stock')
            o=Order.objects.create(reference='SF-'+uuid.uuid4().hex[:8].upper(),product=p,quantity=qty,unit_price=p.price,customer=customer[:120])
        return JsonResponse(order_dict(o),status=201)
    except (KeyError,ValueError,TypeError,Product.DoesNotExist):return error('Invalid order data')
def summary(request):
    ps=list(Product.objects.all());os=list(Order.objects.all())
    return JsonResponse({'products':len(ps),'units':sum(p.stock for p in ps),'inventory_value':str(sum((p.stock*p.price for p in ps),Decimal(0))),'low_stock':sum(p.stock<=p.reorder_level for p in ps),'orders':len(os),'sales':str(sum((o.quantity*o.unit_price for o in os),Decimal(0)))})
def export(request):
    response=HttpResponse(content_type='text/csv');response['Content-Disposition']='attachment; filename="stockflow-inventory.csv"'
    writer=csv.writer(response);writer.writerow(['SKU','Product','Category','Price INR','Stock'])
    for p in Product.objects.order_by('sku'):writer.writerow([p.sku,p.name,p.category,p.price,p.stock])
    return response
