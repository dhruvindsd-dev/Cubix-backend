from product.models import Product
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
# Create your models here.

# using the default djngo user model


@receiver(post_save, sender=User)
def createAuthToken(sender, instance=None, created=False, **kwargs):
    if created:
        WishList.objects.create(user=instance)
        Cart.objects.create(user=instance)
        Token.objects.create(user=instance)


class WishList(models   .Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


class Order(models.Model):
    title = models.CharField(max_length=50)
    productId = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(default=2)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
