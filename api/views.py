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
        return self.request.user.profile

class Donation(CreateAPIView):
    serializer_class = DonationSerializer
    def create(self, request, *args, **kwargs):
        serializer = DonationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_data = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(DonationSerializer(new_data).data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        donation,created = Donation.objects.get_or_create(user=self.request.user, active=True)
        return serializer.save(donation = donation)

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


