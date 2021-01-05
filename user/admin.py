from django.contrib import admin
from .models import WishList, Cart, Order
# Register your models here.


admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Order)
