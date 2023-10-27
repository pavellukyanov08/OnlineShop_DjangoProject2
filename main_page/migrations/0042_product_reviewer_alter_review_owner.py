# Generated by Django 4.2.4 on 2023-10-08 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main_page', '0041_alter_product_options_product_vote_ratio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
