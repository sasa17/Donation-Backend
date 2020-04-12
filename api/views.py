from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from datetime import date

from .serializers import UserCreateSerializer, DonationSerializer, ProfileSerializer,RestaurantSerializer,RestaurantDetailSerializer,MenuUpdateSerializer,DonationBasketAddSerializer,DonationBasketSerializer,MenuAddSerializer,RestaurantProfileSerializer
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
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class RestaurantProfileDetails(RetrieveAPIView):
    serializer_class = RestaurantProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.restaurant
    

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

class DonationBasketList(ListAPIView):
	serializer_class = DonationBasketSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return DonationBasket.objects.filter(restaurant=self.request.user.restaurant)

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

class DonationList(ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Donation.objects.filter(date= date.today(),active = False)


