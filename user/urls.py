from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up', signUp),
    path('get-token', getToken),
    path('get-user-cart', getUserCart),
    path('get-user-wishlist', getUserWishList),
    path('get-user-orders', getUserOrders),
    path('cart/<str:type>/<int:id>', handleCart),
    path('wishList/<str:type>/<int:id>', handleWishList),
    path('place-order', handleOrders),

]
