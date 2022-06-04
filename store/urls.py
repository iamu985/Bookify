from django.contrib import admin
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug:category_slug>', views.category_view, name='category'),
    path('product/<slug:product_slug>', views.product_view, name='product')
]

