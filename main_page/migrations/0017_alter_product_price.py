# Generated by Django 4.2.4 on 2023-10-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=6, null=True, verbose_name='Цена (руб)'),
        ),
    ]