# Generated by Django 4.2.4 on 2023-10-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_comparison', '0008_remove_compare_height_remove_compare_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compare',
            name='height',
            field=models.CharField(max_length=10, null=True, verbose_name='Высота (см)'),
        ),
        migrations.AddField(
            model_name='compare',
            name='img',
            field=models.ImageField(null=True, upload_to='main_page/images', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='compare',
            name='price',
            field=models.CharField(max_length=10, null=True, verbose_name='Цена (руб)'),
        ),
        migrations.AddField(
            model_name='compare',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compare',
            name='weight',
            field=models.CharField(max_length=10, null=True, verbose_name='Вес (кг)'),
        ),
        migrations.AddField(
            model_name='compare',
            name='width',
            field=models.CharField(max_length=10, null=True, verbose_name='Ширина (см)'),
        ),
        migrations.AlterField(
            model_name='compare',
            name='product',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Наименование'),
        ),
    ]
