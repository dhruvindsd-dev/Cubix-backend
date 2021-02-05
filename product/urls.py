from django.urls import path
from .views import *

urlpatterns = [
    path('home-page', get_home_page_content),
    path('get-product-data/<int:id>', get_product_data),
    path('product-search', product_search),
]
