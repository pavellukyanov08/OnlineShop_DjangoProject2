# Generated by Django 4.2.4 on 2023-10-06 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0035_rename_product_availability_product_availability_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]