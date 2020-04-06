from django.contrib import admin
from .models import Restaurant, Menu, Donation,DonationBasket


admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Donation)
admin.site.register(DonationBasket)

