from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem

# Create your views here.


def say_hello(request):
    customer_queryset = Customer.objects.filter(email__icontains='.com')

    collection_queryset = Collection.objects.filter(
        featured_product__isnull=True)

    product_queryset = Product.objects.filter(inventory__lt=10)

    order_queryset = Order.objects.filter(customer_id=1)

    orderItem_queryset = OrderItem.objects.filter(product__collection__id=3)

    return render(request, 'hello.html', {"name": "I Nyoman Warsana", "customers": list(customer_queryset)})
