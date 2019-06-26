from django.db import connection
from django.shortcuts import render
from . models import Book,BookOrder,Publisher,Author
from django.http import HttpResponse
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
# Create your views here.

def index(request):
    result=Book.objects.aggragate(Avg("bookorder__price"))
    print(result)
    print(connection.queries)

    books=Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
