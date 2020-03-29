from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name,
                        last_name=last_name, email=email)
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
