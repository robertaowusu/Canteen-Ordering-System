from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    nutritional_info = models.TextField()
    
    def __str__(self):
        return self.name
    
