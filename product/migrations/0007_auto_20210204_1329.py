# Generated by Django 3.1.2 on 2021-02-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210204_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Product images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
