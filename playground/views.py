from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(description__isnull=True)

    return render(request, 'hello.html', {"name": "I Nyoman Warsana", "products": list(queryset)})
