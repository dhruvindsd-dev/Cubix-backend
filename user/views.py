from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from .models import Cart, WishList, Order
from product.serializer import ProductCardSerialiazer
from .serializers import OrderSerializer


def handle_cart_while_auth(userCart, user):
    userCart = userCart.split(',')
    if userCart[0] == '':
        return
    cart = Cart.objects.get(user=user)
    for productId in userCart:
        try:
            product = Product.objects.get(id=int(productId))
        except:
            pass
        else:
            cart.products.add(product)


@api_view(['POST'])
def sign_up(request):
    data = request.data
    # username, email, password, firstname, lastname
    if 'username' in data and 'password' in data and 'email' in data and 'firstName' in data and 'lastName' in data and 'cart' in data:
        try:
            user = User.objects.get(username=request.data['username'])
        except:
            # some error occured and the user doesnt exist, create a user in that case
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email'],
                first_name=request.data['firstName'],
                last_name=request.data['lastName'],
            )
            handle_cart_while_auth(data['cart'], user)
            token = Token.objects.get(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        else:
            # user aldready exists.
            return Response({
                'error': 'user_exists'
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'error': 'invalid_fields',
        },
            status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_token(request):
    # sign in
    data = request.data
    if 'username' in data and 'password' in data and 'cart' in data:
        user = authenticate(
            username=data['username'], password=data["password"])
        if user is not None:
            token = Token.objects.get(user=user)
            handle_cart_while_auth(data['cart'], user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            # the credentials are invalid.
            return Response({'error': 'invalid_credentials'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({
            'error': 'invalid_fields'
        }, status=status.HTTP_400_BAD_REQUEST)


# # add,removew from cart and wishlist
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def handle_cart(request, type, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({"error": "invalid id"})
    else:
        print(request.user)
        cart = Cart.objects.get(user=request.user)
        if type == 'add':
            cart.products.add(product)
            cart.save()
            return Response({'product added'}, status=status.HTTP_200_OK)
        elif type == 'remove':
            cart.products.remove(product)
            cart.save()
            return Response("product removed", status=status.HTTP_200_OK)
        else:
            return Response("invalid action", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def handle_wish_list(request, type, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response("invalid id ")
    else:
        wishlist = WishList.objects.get(user=request.user)
        if type == 'add':
            wishlist.products.add(product)
            wishlist.save()
            return Response("product added", status=status.HTTP_200_OK)
        elif type == 'remove':
            wishlist.products.remove(product)
            wishlist.save()
            return Response("product removed", status=status.HTTP_200_OK)
        else:
            return Response("invalid action", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_cart(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.products.all()
    products = ProductCardSerialiazer(products, many=True)
    return Response({'products': products.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_wish_list(request):
    wishlist = WishList.objects.get(user=request.user)
    products = wishlist.products.all()
    products = ProductCardSerialiazer(products, many=True)
    return Response(products.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_orders(request):
    orders = Order.objects.filter(user=request.user)
    orders = OrderSerializer(orders, many=True)
    return Response(orders.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def handle_orders(request):
    cart = Cart.objects.get(user=request.user)
    # add cart products to orders
    for product in cart.products.all():
        Order.objects.create(title=product.title, productId=product.id,
                             imgLink=str(product.img),
                             price=product.price, discount=product.discount, user=request.user)
    # clear cart after placing the order
    cart.products.clear()
    cart.save()
    return Response("order placed", status=status.HTTP_200_OK)
