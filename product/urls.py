from django.urls import path
from .views import *

urlpatterns = [
    path('home-page', getHomePageContent),
    path('get-product-data/<int:id>', productData),
    path('product-search', productSearch),
]
