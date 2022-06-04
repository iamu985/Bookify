from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['in_stock', 'is_active']
    list_display = ['category', 'created_by', 'author', 'slug', 'price', 'created', 'updated']
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
