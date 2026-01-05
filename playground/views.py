from django.shortcuts import render
from django.db import connection


def say_hello(request):
    with connection.cursor() as cursor:
        cursor.callproc('get_customers', [1])

        return render(request, 'hello.html', {"name": "I Nyoman Warsana", })
