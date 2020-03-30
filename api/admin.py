from django.contrib import admin
from .models import Cart, CartItem,Menu,Restaurant


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Menu)
admin.site.register(Restaurant)
