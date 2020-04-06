from .models import Donation, DonationBasket, Restaurant
import date from datetime

def get_total_donations():
    restaurants = Restaurant.objects.all()
    donation_basket_total = 0
    donation_total = 0
    all_donations = Donation.objects.filter(date=date.today(), active=False)
    for donation in all_donations:
        donation_total+=donation.amount
    for restaurant in restaurants:
        donationbasket=DonationBasket.objects.get(restaurant=restaurant,date=date.today())
        donation_basket_total+=donationbasket.single_restaurant_total
    for restaurant in restaurants:
        donation_basket = DonationBasket.objects.get(date=date.today(),restaurant=restaurant)
        donation_basket.total_donation_recieved = donation_total* (donation_basket.single_restaurant_total/donation_basket_total)
        donation_basket.save()



        

    
