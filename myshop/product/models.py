from django.db import models

CATEGORY_CHOICES = (
    ('O','Outer'),
    ('T','Top'),
    ('S', 'Skirt'),
    ('P', 'Pants')
)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=False)
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products')

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.title