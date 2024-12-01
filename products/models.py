from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(),
    quantity = models.IntegerField(default=1),
    description = models.TextField(max_length=5000, blank=True),
    # TODO: use file for picture (pillow library)
    picturePath = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}$"