from django.contrib import admin
from .models import Restaurant, Menu, Cart, CartItem

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Cart)
admin.site.register(CartItem)
