# Generated by Django 4.2.4 on 2023-10-28 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0019_alter_favourite_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favourite',
            options={'ordering': ('product',), 'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.RenameField(
            model_name='favourite',
            old_name='products',
            new_name='product',
        ),
    ]
