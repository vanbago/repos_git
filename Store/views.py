from django.shortcuts import render
from Store.models import product

# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request, 'index.html', context={"products" : products})
