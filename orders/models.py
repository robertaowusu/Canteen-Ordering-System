from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('Preparing', 'Preparing'), ('Ready', 'Ready for Pickup')])
    loyalty_points = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"