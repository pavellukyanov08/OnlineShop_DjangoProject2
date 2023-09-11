from django.db import models
from django.contrib.auth.models import User


class Favourite(models.Model):
    product = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', null=True)
    description = models.TextField(max_length=350, verbose_name='Описание', null=True)
    img = models.ImageField(upload_to='main_page/images', verbose_name='Изображение', null=True)
    price = models.CharField(max_length=10, verbose_name='Цена', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product

