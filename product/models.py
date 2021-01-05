from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

typeChoice = (
    ('general', 'general'),
    ('trending', 'trending'),
    ('top_sellers', 'top_sellers'),
    ('best_cubes', 'best_cubes')
)
catagory_choice = (
    ('Standard Speed Cube', 'Standard Speed Cube'),
    ('Pyramix', 'Pyramix'),
    ('Megamix', 'Megamix'),
    ('Skewb', 'Skewb'),
    ('Square-1', 'Square-1'),
    ('Magic Cube', 'Magic Cube'),
    ('Gear Cube', 'Gear Cube'),
    ('Locking Puzzels', 'Locking Puzzels'),
)


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    rating = models.IntegerField(default=3, validators=[
        MaxValueValidator(5), MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    avalibility = models.BooleanField(default=False)
    max_order_quantity = models.IntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    returnable = models.BooleanField(default=False)
    no_contact_delivery = models.BooleanField(default=True)
    weight_kg = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)])
    color = models.CharField(max_length=20, default='No available')
    # featured =
    type = models.CharField(
        choices=typeChoice, max_length=50, default='general')
    # catagory = m odels.CharField(max_length=50, choices=catagory_choice)
