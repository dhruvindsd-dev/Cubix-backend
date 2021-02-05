from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up', sign_up),
    path('get-token', get_token),
    path('get-user-cart', get_user_cart),
    path('get-user-wishlist', get_user_wish_list),
    path('get-user-orders', get_user_orders),
    path('cart/<str:type>/<int:id>', handle_cart),
    path('wishList/<str:type>/<int:id>', handle_wish_list),
    path('place-order', handle_orders),

]
