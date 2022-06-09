from django.db import models
from store.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    cart_no = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_buy = models.BooleanField(default=False)

    def __str__(self):
        return f"C-{self.cart_no}-{self.product.title}"
    