# Generated by Django 3.1.2 on 2021-01-01 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=350)),
                ('rating', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('avalibility', models.BooleanField(default=False)),
                ('max_order_quantity', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('returnable', models.BooleanField(default=False)),
                ('no_contact_delivery', models.BooleanField(default=True)),
                ('weight_kg', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)])),
                ('color', models.CharField(default='No available', max_length=20)),
                ('type', models.CharField(choices=[('general', 'general'), ('trending', 'trending'), ('top_sellers', 'top_sellers'), ('best_cubes', 'best_cubes')], default='general', max_length=50)),
            ],
        ),
    ]
