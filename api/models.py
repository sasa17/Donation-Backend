from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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



class CartItem(models.Model):
    menu_item = models.ForeignKey(
        Menu, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s: %s" % (self.menu_item.name, str(self.quantity))


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField()

    def __str__(self):
        return self.user.username
