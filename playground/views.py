from django.shortcuts import render
from django.db.models import Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer

# Create your views here.


def say_hello(request):

    # queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField())

    queryset = Product.objects.annotate(discounted_price=discounted_price)

    return render(request, 'hello.html', {"name": "I Nyoman Warsana", "result": list(queryset)})
