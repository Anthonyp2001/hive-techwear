from django.db import models
from apps.user.models import User
from apps.products.models import Product

class Cart(models.Model):
    class Meta(object):
        db_table = 'cart'

    user = models.ForeignKey(
        User, related_name='related_user', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='related_products', on_delete=models.CASCADE
    )
    quantity = models.IntegerField (
        'Quantity', blank=False, null=False
    )

    @property
    def total_price(self):
        return self.quantity * self.product.price


