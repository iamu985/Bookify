from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from .models import Cart

def cart_view(request):
    products_in_cart = Cart.objects.all()
    context = {'products':products_in_cart}
    return render(request, 'cart/cart-view.html', context)

def add_cart(request, product_slug):
    # enter into cart database
    user = request.user
    carted_product = Product.objects.get(slug=product_slug)
    new_cart_product = Cart.objects.create(product=carted_product, user=user)
    new_cart_product.save()
    return redirect('cart:cart_view')

def delete_cart(request, cart_id):
    cart_product = Cart.objects.get(pk=cart_id)
    cart_product.delete()
    print('Cart deleted')
    return redirect('cart:cart_view')
