from rest_framework import serializers
from .models import User, Car, Trip, UserRoute


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
