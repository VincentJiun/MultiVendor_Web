from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Product, Category

# Create your views here.

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'store/product_detail.html', {
        'product': product
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    return render(request, 'store/category_detail.html', {
        'category': category,
        'products': products
    })

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'store/vendor_detail.html', {
        'user': user
    })