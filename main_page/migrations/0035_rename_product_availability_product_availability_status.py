# Generated by Django 4.2.4 on 2023-10-06 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0034_rename_status_choices_productavailability_availability_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_availability',
            new_name='availability_status',
        ),
    ]