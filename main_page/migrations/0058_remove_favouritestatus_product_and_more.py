# Generated by Django 4.2.7 on 2023-11-15 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0057_favouritestatus_comparestatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouritestatus',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favouritestatus',
            name='user',
        ),
        migrations.DeleteModel(
            name='CompareStatus',
        ),
        migrations.DeleteModel(
            name='FavouriteStatus',
        ),
    ]
