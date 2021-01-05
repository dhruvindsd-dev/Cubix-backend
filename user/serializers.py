from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order
from product.serializer import ProductCardSerialiazer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')
