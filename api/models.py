from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Donation(models.Model):
    user = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateField(default=date.today)
    active = models.NullBooleanField() 

    def __str__(self):
        return "%s: %s" % (self.user.username, str(self.amount))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone = models.CharField(max_length=8)

    def __str__(self):
        return str(self.user)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()
   
    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    name = models.CharField(max_length=250)
    original_price = models.DecimalField(max_digits=10, decimal_places=3)
    discount = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    available_qty = models.PositiveIntegerField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
