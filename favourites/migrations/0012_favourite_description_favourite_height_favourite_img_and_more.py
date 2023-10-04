# Generated by Django 4.2.5 on 2023-09-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0011_remove_favourite_description_remove_favourite_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='description',
            field=models.TextField(max_length=350, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='height',
            field=models.CharField(max_length=10, null=True, verbose_name='Высота (см)'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='img',
            field=models.ImageField(null=True, upload_to='main_page/images', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='price',
            field=models.CharField(max_length=10, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='weight',
            field=models.CharField(max_length=10, null=True, verbose_name='Вес (кг)'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='width',
            field=models.CharField(max_length=10, null=True, verbose_name='Ширина (см)'),
        ),
    ]