from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


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
