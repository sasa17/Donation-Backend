from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

# Create your models here.

class Donation(models.Model):
    user = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateField(default=date.today)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s: %s" % (self.user.username, str(self.amount))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=None)


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
    discount = models.DecimalField(default=0,max_digits=10, decimal_places=3)
    description = models.TextField()
    image = models.ImageField()
    available_qty = models.PositiveIntegerField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return str(self.name)


class DonationBasket(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    single_restaurant_total = models.DecimalField(default=0,max_digits=10, decimal_places=3)
    date = models.DateField(default=date.today)
    total_donation_recieved = models.DecimalField(default=0,max_digits=10, decimal_places=3)

    def __str__(self):
        return "%s: %s" % (str(self.date), self.restaurant.name)

@receiver(pre_save, sender=Menu)
def get_total(instance, *args, **kwargs):
    instance.total = (instance.original_price*((100-instance.discount)/100))* instance.available_qty

class Checkout(models.Model):
    amount = models.ForeignKey(Donation, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return "%s: %s" % (str(self.date), str(self.donation.amount))

@receiver(pre_save, sender=Donation)
def get_total(instance, *args, **kwargs):
    instance.total += instance.amount
