from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, DecimalField
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

# Create your views here.
queryset = TaggedItem.objects.get_tags_for(Product, 1)


def say_hello(request):

    return render(request, 'hello.html', {"name": "I Nyoman Warsana", "result": list(queryset)})
