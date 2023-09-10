# Generated by Django 4.2.5 on 2023-09-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50, verbose_name='Наименование')),
                ('price', models.CharField(max_length=20)),
                ('img', models.ImageField(null=True, upload_to='main_page/images')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]