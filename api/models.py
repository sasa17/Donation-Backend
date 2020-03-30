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


# class Cart_Item(models.Model):
#     item = models.ForeignKey(
#         Item, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return "%s: %s" % (self.item.name, str(self.quantity))


# class Cart(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE)
#     cart_item = models.ForeignKey(
#         Cart_Item, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     active = models.BooleanField()

#     def __str__(self):
#         return self.user.username
