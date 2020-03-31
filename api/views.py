from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import UserCreateSerializer, DonationSerializer, ProfileSerializer,RestaurantSerializer,RestaurantDetailSerializer
from .models import Donation, Restaurant
from .permissions import IsCartOwner

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProfileDetails(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

class DonationItem(CreateAPIView):
    serializer_class = DonationSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, active=True)
        
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
    permission_classes = [IsAuthenticated]

class RestaurantDetail(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'
	permission_classes = [IsAuthenticated]


