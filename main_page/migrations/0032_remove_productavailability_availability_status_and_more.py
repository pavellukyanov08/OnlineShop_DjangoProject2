# Generated by Django 4.2.4 on 2023-10-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0031_productavailability_status_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productavailability',
            name='availability_status',
        ),
        migrations.RemoveField(
            model_name='productavailability',
            name='status_choices',
        ),
    ]