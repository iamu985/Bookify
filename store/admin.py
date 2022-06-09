from django.contrib import admin
from .models import Product, Category, Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['in_stock', 'is_active']
    list_display = ['title', 'category', 'created_by', 'author', 'slug', 'price', 'created', 'updated']
    prepopulated_fields = {'slug':('title',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'ordered_on', 'quantity', 'status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
