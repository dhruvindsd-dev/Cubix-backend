from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Product
from .serializer import ProductCardSerialiazer, ProductPageSerialiazer


@api_view(['GET'])
def get_home_page_content(request):
    # geting all the types excluding the general one
    trendingCubes = Product.objects.all().filter(popularity="trending")
    topSellingCubes = Product.objects.all().filter(popularity="top_sellers")
    bestCubes = Product.objects.all().filter(popularity="best_cubes")

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
        # also send some product recomendations, 3 cubes in the same catagory or any catagory
        recomendations = Product.objects.filter(
            catagory=product.catagory).exclude(id=product.id)
        recomendations = ProductCardSerialiazer(recomendations, many=True)
        product = ProductPageSerialiazer(product)
    return Response({
        "product": product.data,
        "recomendation": recomendations.data
    })


@api_view(['GET'])
def product_search(request):
    # if keyword in title or description
    data = request.GET
    if 'search' in data and 'catagory' in data:
        keywords = data.get('search').split(' ')
        catagory = data.get('catagory')
        titleQ = Q()
        descriptionQ = Q()
        catagoryQ = Q(catagory=catagory)
        for keyword in keywords:
            titleQ = titleQ & Q(title__contains=keyword)
            descriptionQ = descriptionQ & Q(description__contains=keyword)
        if keywords[0] == '' and catagory != 'all':
            product = Product.objects.filter(catagoryQ)
        elif catagory == 'all':
            product = Product.objects.filter(titleQ | descriptionQ)
        else:
            product = Product.objects.filter(
                (titleQ | descriptionQ) & catagoryQ)
        product = ProductCardSerialiazer(product, many=True)
        return Response({'products': product.data})
    else:
        return Response('invalid fields')
