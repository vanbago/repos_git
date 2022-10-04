from django.shortcuts import get_object_or_404, render
from Store.models import product
#from django.http import HttpResponse

# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request, 'index.html', context={"products" : products})


def product_detail(request, slug):
    products = get_object_or_404(product, slug = slug)
    return  render(request, "new.html", context={"products": products})
