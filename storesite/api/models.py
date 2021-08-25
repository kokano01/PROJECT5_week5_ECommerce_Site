from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 255)
    image = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    

    def __str__(self):
        return f'{self.name}'
