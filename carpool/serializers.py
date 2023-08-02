from rest_framework import serializers
from .models import User, Car, Trip, UserRoute


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class UserRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoute
        fields = "__all__"
