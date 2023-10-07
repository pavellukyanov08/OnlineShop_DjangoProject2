from django.db import models
from django.contrib.auth.models import User
from main_page.models import Category, Product


class Compare(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование', null=True)
    # slug = models.SlugField(max_length=100, db_index=True, null=True)
    # img = models.ImageField(upload_to='main_page/images', verbose_name='Изображение', null=True)
    # width = models.CharField(max_length=10, verbose_name='Ширина (см)', null=True)
    # height = models.CharField(max_length=10, verbose_name='Высота (см)', null=True)
    # weight = models.CharField(max_length=10, verbose_name='Вес (кг)', null=True)
    # price = models.CharField(max_length=10, verbose_name='Цена (руб)', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('product',)
        verbose_name = 'Сравнение товара'
        verbose_name_plural = 'Сравнение товаров'

    def __str__(self):
        return self.product

