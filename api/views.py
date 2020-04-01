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
    permission_classes = [IsAuthenticated]

class RestaurantDetail(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'
	permission_classes = [IsAuthenticated]


