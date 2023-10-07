# Generated by Django 4.2.5 on 2023-09-30 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_alter_product_category'),
        ('favourites', '0013_alter_favourite_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='description',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='height',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='img',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='price',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='width',
        ),
        migrations.AlterField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.product', verbose_name='Наименование'),
        ),
    ]
