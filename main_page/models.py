from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('main_page:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Продукты', null=True)
    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', null=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True)
    description = models.TextField(max_length=350, verbose_name='Описание', null=True)
    img = models.ImageField(upload_to='main_page/images', verbose_name='Изображение', null=True)
    width = models.CharField(max_length=10, verbose_name='Ширина (см)', null=True)
    height = models.CharField(max_length=10, verbose_name='Высота (см)', null=True)
    weight = models.CharField(max_length=10, verbose_name='Вес (кг)', null=True)
    price = models.CharField(max_length=10, verbose_name='Цена (руб)', null=True)
    discount_price = models.CharField(max_length=10, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('name',)
        index_together = ('id', 'slug',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('main_page:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
