# Generated by Django 4.2.4 on 2023-10-05 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0028_remove_product_available_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productavailability',
            options={'verbose_name': 'Статус наличия', 'verbose_name_plural': 'Статусы наличия'},
        ),
    ]