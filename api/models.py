from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Restaurant(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()

class Menu(models.Model):
    name = models.CharField(max_length=250)
    original_price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    image = models.ImageField()
    available_qty = models.PositiveIntegerField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)

