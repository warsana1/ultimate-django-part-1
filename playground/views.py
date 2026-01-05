from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, 'hello.html', {"name": "I Nyoman Warsana", })
