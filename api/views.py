from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from datetime import date

from .serializers import UserCreateSerializer, DonationSerializer, ProfileSerializer,RestaurantSerializer,RestaurantDetailSerializer,MenuUpdateSerializer,DonationBasketAddSerializer,DonationBasketSerializer,MenuAddSerializer
from .models import Donation, Restaurant,Menu,DonationBasket
from .permissions import IsCartOwner

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from decimal import Decimal


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProfileDetails(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

class UpdateMenu(RetrieveUpdateAPIView):
    serializer_class = MenuUpdateSerializer
    queryset = Menu.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'menu_id'
    permission_classes = [IsAuthenticated]

class DonationBasketAdd(CreateAPIView):
    serializer_class = DonationBasketAddSerializer

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(user=self.request.user)
        items = Menu.objects.filter(restaurant = restaurant.id)
        single_restaurant_amount = 0
        for item in items:
            single_restaurant_amount += item.total
        return serializer.save(single_restaurant_total = single_restaurant_amount,restaurant=restaurant)



class MenuAdd(CreateAPIView):
    serializer_class = MenuAddSerializer

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(user=self.request.user)
        original_price = Decimal(self.request.data.get('original_price'))
        discount = Decimal(self.request.data.get('discount'))
        available_qty = Decimal(self.request.data.get('available_qty'))
        total = (original_price*((100-discount)/100))* available_qty
        return serializer.save(total = total,restaurant = restaurant)

class DonationBasketDetail(RetrieveAPIView):
    serializer_class = DonationBasketSerializer
    queryset = DonationBasket.objects.all()
    lookup_field = 'restaurant'
    lookup_url_kwarg = 'restaurant_id'
    permission_classes = [IsAuthenticated]

class DonationItem(APIView):
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        donation = Donation.objects.filter(user=request.user, active=True).first()
        if serializer.is_valid():
            if Donation.objects.filter(user=request.user, active=True).exists():
                donation.amount = request.data.get('amount')
                new_data = DonationSerializer(donation)
                donation.save()
                return Response(new_data.data, status=status.HTTP_201_CREATED)
            serializer.save(user=request.user, active=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonationBasketView(APIView):

    def get(self, request):
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

class Checkout(APIView):
    serializer_class = DonationSerializer
    def get(self, request):
        donation = Donation.objects.get(user=request.user, active=True)
        donation.active = False
        donation.save()
        return Response(DonationSerializer(donation).data)

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'


