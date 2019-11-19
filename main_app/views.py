from django.shortcuts import render
from .models import Search

from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def product_form(request):
    search = Search.objects.all()
    return render(request, 'product_form.html')

class CreateProduct(CreateView):
    model= Search
    fields = '__all__'
    template_name = 'add.html'
    success_url = '/product_form'