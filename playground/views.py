from django.shortcuts import render
from django.db.models.aggregates import Count, Min
from store.models import Product

# Create your views here.


def say_hello(request):

    result = Product.objects.filter(collection__id=1).aggregate(
        count=Count('id'), min_price=Min('unit_price'))

    return render(request, 'hello.html', {"name": "I Nyoman Warsana", "result": result})
