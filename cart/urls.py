from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('cart-view/', views.cart_view, name="cart_view"),
    path('add-to-cart/<slug:product_slug>', views.add_cart, name="add_cart"),
    path('delete-cart/<int:cart_id>', views.delete_cart, name="delete_cart"),
]
