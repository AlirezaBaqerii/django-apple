from django.db import models

from apps.store.models import Product


class BagModel(models.Model):
    product_id = models.IntegerField()

    def __str__(self):
        return Product.objects.get(id=self.product_id)
