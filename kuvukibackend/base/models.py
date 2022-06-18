from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name