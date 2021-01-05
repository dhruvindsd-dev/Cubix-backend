from rest_framework import serializers
from .models import Product


class ProductCardSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'discount', 'rating', "id", "avalibility")
        # todo img ...


class ProductPageSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
