from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, CartItem, Cart
from datetime import date


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'phone', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        phone = validated_data['phone']
        new_user = User(username=username, first_name=first_name,
                        last_name=last_name, email=email, phone=phone)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    past_items = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['user']


class CartItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.SlugRelatedField(slug_field='name', read_only=True)
    item_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['menu_item', 'quantity','item_price','id']

    def get_item_price(self, obj):
        return obj.item.price*obj.quantity


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cart_item = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'id', 'date', 'cart_item']

    def get_cart_item(self, obj):
        cart_item = CartItem.objects.filter(cart=obj.id)
        return CartItemSerializer(cart_item, many=True).data


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['item', 'quantity']


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
