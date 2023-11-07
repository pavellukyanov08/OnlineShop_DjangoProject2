# Generated by Django 4.2.4 on 2023-10-28 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0054_product_cart_prods'),
        ('favourites', '0020_alter_favourite_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.product', verbose_name='Продукт'),
        ),
    ]