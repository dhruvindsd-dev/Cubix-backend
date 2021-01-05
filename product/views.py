from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import ProductCardSerialiazer, ProductPageSerialiazer
from .models import Product
from django.db.models import Q


@api_view(['GET'])
def getHomePageContent(request):
    # geting all the types excluding the general one
    trendingCubes = Product.objects.all().filter(type="trending")
    topSellingCubes = Product.objects.all().filter(type="top_sellers")
    bestCubes = Product.objects.all().filter(type="best_cubes")
    # serialize everything
    trendingCubes = ProductCardSerialiazer(trendingCubes, many=True)
    topSellingCubes = ProductCardSerialiazer(topSellingCubes, many=True)
    bestCubes = ProductCardSerialiazer(bestCubes, many=True)
    return Response({
        "Trending Cubes": trendingCubes.data,
        "Top Selling Cubes": topSellingCubes.data,
        "Our Best Cubes": bestCubes.data
    })


@api_view(['GET'])
def productData(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({'error': 'invalid id'})
    else:
        product = ProductPageSerialiazer(product)
    return Response({
        "product": product.data
    })


@api_view(['GET'])
def productSearch(request):
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
