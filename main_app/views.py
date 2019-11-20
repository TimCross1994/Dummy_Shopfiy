from django.shortcuts import render
from .models import Search

from django.http import HttpResponse


def product_form(request):
    search = Search.objects.all()
    return render(request, 'product_form.html')

