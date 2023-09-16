from django.db import models
from django.contrib.auth.models import User
from main_page.models import Category


class Favourite(models.Model):
    product = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', null=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True)
    description = models.TextField(max_length=350, verbose_name='Описание', null=True)
    width = models.CharField(max_length=10, verbose_name='Ширина (см)', null=True)
    height = models.CharField(max_length=10, verbose_name='Высота (см)', null=True)
    weight = models.CharField(max_length=10, verbose_name='Вес (кг)', null=True)
    img = models.ImageField(upload_to='main_page/images', verbose_name='Изображение', null=True)
    price = models.CharField(max_length=10, verbose_name='Цена', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('product',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


    def __str__(self):
        return self.product

