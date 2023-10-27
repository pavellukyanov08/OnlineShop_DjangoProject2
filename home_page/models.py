from django.db import models
from shopping_cart.models import ShoppingCart


class Home:
    card_prod = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)