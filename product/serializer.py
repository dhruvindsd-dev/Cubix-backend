from rest_framework import serializers
from .models import Product


class ProductCardSerialiazer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return f'http://127.0.0.1:8000/{obj.img}'

    class Meta:
        model = Product
        fields = ('title', 'price', 'discount',
                  'rating', "id", "avalibility", 'img')
        # todo img ...


class ProductPageSerialiazer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return f"http://127.0.0.1:8000/{obj.img}"

    class Meta:
        model = Product
        fields = ('__all__')
