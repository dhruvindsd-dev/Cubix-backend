# Generated by Django 3.1.2 on 2021-02-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('Standard Speed Cube', 'Standard Speed Cube'), ('Pyramix', 'Pyramix'), ('Megamix', 'Megamix'), ('Skewb', 'Skewb'), ('Square-1', 'Square-1'), ('Magic Cube', 'Magic Cube'), ('Gear Cube', 'Gear Cube'), ('Locking Puzzels', 'Locking Puzzels')], default='general', max_length=50),
            preserve_default=False,
        ),
    ]
