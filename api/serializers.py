from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Donation,Restaurant,Menu, DonationBasket
from datetime import date


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password'] #'phone']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        # phone = validated_data['phone']
        new_user = User(username=username, first_name=first_name,
                        last_name=last_name, email=email) #phone=phone)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    past_donations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'past_donations'] #, 'phone'

    def get_past_donations(self, obj):
        amount = Donation.objects.filter(user=obj, date__lte=date.today(), active=False)
        return DonationSerializer(amount, many=True).data


class DonationSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    class Meta:
        model = Donation
        fields = ['amount', 'user', 'active', 'id', 'date']
    def get_total(self, obj):
        for amount in self:
            return total + obj.amount

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'description', 'image','id']

class MenuSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id','name', 'original_price', 'discount','discounted_price','description','image','available_qty','total','restaurant']

    def get_discounted_price(self, obj):
        return obj.original_price*((100-obj.discount)/100)
    
    def get_total(self, obj):
        return (obj.original_price*((100-obj.discount)/100))*obj.available_qty
    
class MenuUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['available_qty']

class RestaurantDetailSerializer(serializers.ModelSerializer):
    menu = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'description', 'image','id','menu']

    def get_menu(self,obj):
        menu = Menu.objects.filter(restaurant=obj.id)
        return MenuSerializer(menu, many=True).data

class DonationBasketSerializer(serializers.ModelSerializer):
    total_donations = DonationSerializer()
    restaurant_total = serializers.SerializerMethodField()
    amount_donated = serializers.SerializerMethodField()
    item = MenuSerializer()
    single_restaurant_total = serializers.SerializerMethodField()

    class Meta:
        model = DonationBasket
        fields = ['restaurant', 'date', 'item_total', 'amount_donated','id']

    def get_item_total(self, obj):
        for items in self.item:
            return item_total + self.item.total
    
    def get_restaurant_total(self,obj):
        for restaurant in single_restaurant_total:
            return restaurant_total + self.single_restaurant_total.total
    
    def get_total_donations(self, obj):
        total = Donation.objects.filter(date=date.today(), active=False)
        return DonationSerializer(total, many=True).data
    
    def get_amount_donated(self,obj):
        return self.total_donations*(self.single_restaurant_total/self.restaurant_total)

