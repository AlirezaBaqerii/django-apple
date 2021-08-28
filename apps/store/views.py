#from store.context_processors import categories
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/all_products.html', {'products': products})

def filtered_products(request, category_slug):
    selected_category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=selected_category)
    return render(request, 'store/filtered_products.html', {
        'products': products}) 

def single_product(request, product_slug, category_slug):
    print(category_slug)
    product = Product.objects.get(slug=product_slug)
    return render(request, 'store/single.html', {'product': product})
