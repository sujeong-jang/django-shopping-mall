from django.db import models

CATEGORY_CHOICES = (
    ('O','Outer'),
    ('T','Top'),
    ('S', 'Skirt'),
    ('P', 'Pants')
)

class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name