from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Product
from .serializer import ProductCardSerialiazer, ProductPageSerialiazer


@api_view(['GET'])
def get_home_page_content(request):
    # geting all the types excluding the general one
    trendingCubes = Product.objects.all().filter(type="trending")
    topSellingCubes = Product.objects.all().filter(type="top_sellers")
    bestCubes = Product.objects.all().filter(type="best_cubes")

    trendingCubes = ProductCardSerialiazer(trendingCubes, many=True)
    topSellingCubes = ProductCardSerialiazer(topSellingCubes, many=True)
    bestCubes = ProductCardSerialiazer(bestCubes, many=True)
    return Response({
        "Trending Cubes": trendingCubes.data,
        "Top Selling Cubes": topSellingCubes.data,
        "Our Best Cubes": bestCubes.data
    })


@api_view(['GET'])
def get_product_data(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({'error': 'invalid id'})
    else:
        product = ProductPageSerialiazer(product)
    return Response(product.data)


@api_view(['GET'])
def product_search(request):
    # if keyword in title or description
    keywords = request.GET.get('search').split(' ')
    titleQ = Q()
    deescriptionQ = Q()
    for i in keywords:
        titleQ = titleQ & Q(title__contains=i)
        deescriptionQ = deescriptionQ & Q(description__contains=i)
    product = Product.objects.filter(titleQ | deescriptionQ)
    product = ProductCardSerialiazer(product, many=True)
    return Response({'products': product.data})
