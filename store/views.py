from django.shortcuts import render
from .models import Product, Category

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products':products[:4], 'categories':categories[:4]}
    return render(request, 'store/index.html', context=context)

def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    product_in_category = category.product_set.all()
    context = {'products':product_in_category}
    return render(request, 'store/categories.html', context)
    
def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product':product}
    return render(request, 'store/product-view.html', context)