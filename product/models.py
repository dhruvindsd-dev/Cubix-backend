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
    ('Mirror Cube', 'Mirror Cube'),
    ('Gear Cube', 'Gear Cube'),
    ('Locking Puzzels', 'Locking Puzzels'),
)


class Product(models.Model):
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(
        max_length=350, default="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veritatis soluta in placeat et expedita atque ratione dolorem temporibus accusantium, excepturi dicta neque perferendis eaque natus quam quod vel, optio mollitia", blank=True)
    img = models.ImageField(upload_to='Product images', blank=True, null=True)
    rating = models.IntegerField(default=3, validators=[
        MaxValueValidator(5), MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(0)])
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    avalibility = models.BooleanField(default=True)
    max_order_quantity = models.IntegerField(
        default=10, validators=[MaxValueValidator(100), MinValueValidator(1)])
    returnable = models.BooleanField(default=False)
    no_contact_delivery = models.BooleanField(default=True)
    # in grams
    weight = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(1000)], default=200)
    color = models.CharField(max_length=20, default='No available')
    popularity = models.CharField(
        choices=typeChoice, max_length=50, default='general')
    catagory = models.CharField(max_length=50, choices=catagory_choice)

    def __str__(self):
        return self.title + ' - ' + f"[{self.catagory}]"
