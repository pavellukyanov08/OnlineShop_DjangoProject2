from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Menu(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('main_page:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class ProductAvailability(models.Model):
    availability_status = models.CharField(max_length=12, verbose_name='Статус товара', null=True)

    class Meta:
        verbose_name = 'Статус наличия'
        verbose_name_plural = 'Статусы наличия'

    def get_absolute_url(self):
        return reverse('main_page:product_list_by_availability', args=[self.availability_status])

    def __str__(self):
        return self.availability_status


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 verbose_name='Категория')
    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование', null=True)
    slug = models.SlugField(max_length=100, db_index=True, null=True, verbose_name='Слаг')
    description = models.TextField(max_length=350, verbose_name='Описание', null=True)
    img = models.ImageField(upload_to='main_page/images', verbose_name='Изображение', null=True)
    width = models.CharField(max_length=10, verbose_name='Ширина (см)', null=True)
    height = models.CharField(max_length=10, verbose_name='Высота (см)', null=True)
    weight = models.CharField(max_length=10, verbose_name='Вес (кг)', null=True)
    price = models.FloatField(max_length=6, verbose_name='Цена (руб)', null=True)
    discount_price = models.CharField(max_length=10, null=True, verbose_name='Цена со скидкой')
    start_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата старта распродажи')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания распродажи')
    availability_status = models.ForeignKey(ProductAvailability, on_delete=models.CASCADE, null=True, verbose_name='Наличие')
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
