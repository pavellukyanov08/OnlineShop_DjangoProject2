from django.db import models
from django.contrib.auth.models import User


class Compare(models.Model):
    product = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', null=True)
    img = models.ImageField(upload_to='main_page/images', verbose_name='Изображение', null=True)
    price = models.CharField(max_length=10, verbose_name='Цена', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('product',)
        verbose_name = 'Сравнение товара'
        verbose_name_plural = 'Сравнение товаров'

    def __str__(self):
        return self.product

