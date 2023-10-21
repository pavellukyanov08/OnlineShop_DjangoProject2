from django.db import models
from django.urls import reverse
from users.models import Profile
# from shopping_cart.models import ShoppingCart
from django.contrib.auth.models import User


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
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', '-vote_ratio', '-vote_total')
        index_together = ('id', 'slug',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('main_page:product_detail', args=[self.id, self.slug])

    def reviewers(self):
        queryset = self.review_set.all().values_list('reviewer_id', flat=True)
        return queryset

    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_votes = reviews.count()
        ratio = int((up_votes / total_votes) * 100)
        self.vote_total = total_votes
        self.vote_ratio = ratio

        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('За', 'За'),
        ('Против', 'Против')
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Отзыв на')
    body = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    value = models.CharField(max_length=200, choices=VOTE_TYPE, verbose_name='Голос', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = [['owner', 'product'], ]
