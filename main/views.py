from django.shortcuts import render

from store.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()

    return render(request, 'main/index.html', {
        'products': products
    })

def about(request):

    return render(request, 'main/about.html')
