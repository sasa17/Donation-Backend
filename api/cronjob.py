from .models import Donation, DonationBasket, Restaurant
import date from datetime

def get_total_donations():
    restaurants = Restaurant.objects.all()
    donation_basket_total = 0
    all_donations = Donation.filter(date=date.today(), active=False)
    for restaurant in restaurants:
        donation_basket_total += DonationBasket.single_restaurant_total
    for restaurant in restaurants:
        donation_basket = DonationBasket.get(date=date.today(),restaurant=restaurant)
        donation_basket.total_donation_recieved = all_donations* (donation_basket.single_restaurant_total/donation_basket_total)
        donation_basket.save()


        

    
