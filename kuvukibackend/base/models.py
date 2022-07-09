from django.db import models

class Product(models.Model):
    Category = models.TextChoices('Category', 'FRUITS VEGETABLES GROCERIES STATIONERY TOILETRIES BEVERAGES BUTCHERY')

    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    category = models.CharField(blank=True, max_length=15, choices=Category.choices)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='product_images')

    def __str__(self):
        return self.name