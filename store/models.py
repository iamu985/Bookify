from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="images/categories", default="default.png")

    class Meta:
        verbose_name_plural = "categories"
    
    def get_proper_name(self):
        return self.name.title()
    
    def get_absolute_url(self):
        return reverse("store:category", args=[self.slug])
    

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, default="John Doe")
    summary = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/products")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    
    def get_proper_title(self):
        return self.title.title()
    
    def get_absolute_url(self):
        return reverse("store:product", args=[self.slug])
    

    def __str__(self):
        return self.title
    
    

