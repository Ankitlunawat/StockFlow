from django.urls import path
from inventory import views
urlpatterns=[path('',views.index),path('api/products/',views.products),path('api/orders/',views.orders),path('api/summary/',views.summary),path('api/export/',views.export)]
