# Generated by Django 4.2.4 on 2023-10-04 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0006_alter_shoppingcart_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='price',
            field=models.FloatField(max_length=20),
        ),
    ]