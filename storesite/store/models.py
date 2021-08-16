from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length = 255)
    image = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    

    def __str__(self):
        return f'{self.name}'

class Cart(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.username} | {self.product.id}'