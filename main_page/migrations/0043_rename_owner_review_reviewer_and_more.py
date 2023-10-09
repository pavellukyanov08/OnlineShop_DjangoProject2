# Generated by Django 4.2.4 on 2023-10-09 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main_page', '0042_product_reviewer_alter_review_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='owner',
            new_name='reviewer',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('reviewer', 'product')},
        ),
    ]
