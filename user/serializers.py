from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order
from product.serializer import ProductCardSerialiazer
from cubixBackend.settings import HOST_URL


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email')


class OrderSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return f"{HOST_URL}/{obj.imgLink}"

    def get_date(self, obj):
        return obj.date.strftime('%b %y')

    class Meta:
        model = Order
        fields = ('__all__')
