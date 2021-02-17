from rest_framework import serializers
from .models import Product
from cubixBackend.settings import HOST_URL


class ProductCardSerialiazer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return f'{HOST_URL}/{obj.img}'

    class Meta:
        model = Product
        fields = ('title', 'price', 'discount',
                  'rating', "id", "avalibility", 'img')
        # todo img ...


class ProductPageSerialiazer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return f"{HOST_URL}/{obj.img}"

    class Meta:
        model = Product
        fields = ('__all__')
