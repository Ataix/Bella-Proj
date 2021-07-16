from django.contrib.auth import get_user_model
from django.db import models

from core.settings.base import CATEGORY_SEASON_CHOICES, COLOUR_CHOICES

ProfileUser = get_user_model()


class Category(models.Model):
    """
    Model that characterize products' categories
    """
    name = models.CharField(
        max_length=50, unique=True, verbose_name='Название Категории'
    )
    season = models.CharField(
        max_length=50, choices=CATEGORY_SEASON_CHOICES,
        verbose_name='Сезонность категории'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='Родительская катогерия'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название товара')
    article = models.CharField(
        max_length=60, unique=True, verbose_name='Артикул товара'
    )
    quantity = models.IntegerField(verbose_name='Количество в линейке')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Стоимость товара'
    )
    description = models.TextField(verbose_name='О товара')
    size = models.CharField(max_length=60, verbose_name='Размерный ряд')
    structure = models.CharField(max_length=60, verbose_name='Состав ткани')
    length = models.DecimalField(
        max_digits=10, decimal_places=1, verbose_name='Длина'
    )
    style = models.CharField(max_length=60, verbose_name='Фасон')
    discount = models.IntegerField(
        null=True, blank=True, verbose_name='Скидка на товар'
    )
    is_popular = models.BooleanField(
        default=False, verbose_name='Является ли Хитом'
    )
    categories = models.ManyToManyField(
        Category, verbose_name='Категория товара'
    )
    create_date = models.DateTimeField(
        auto_created=True, verbose_name='Время добавления'
    )

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Colour(models.Model):
    """
    Characterizes available colours for products
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Товар'
    )
    name = models.CharField(
        max_length=60, choices=COLOUR_CHOICES, verbose_name='Цвет'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет товара'
        verbose_name_plural = 'Цвета товара'


class Image(models.Model):
    """
    Characterize images of each product
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Товар'
    )
    is_main = models.BooleanField(
        default=False, verbose_name='Является ли главным фото'
    )
    image = models.ImageField(
        upload_to='products/', verbose_name='Изображение'
    )

    def __str__(self):
        return f'{self.product} Image'

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'


class Wish(models.Model):
    """
    Represent wishes of each user
    """
    user = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='Избранный товар пользователя'
    )

    def __str__(self):
        return f"{self.user}'s wish {self.product}"

    class Meta:
        verbose_name = 'Избранное пользователя'
        verbose_name_plural = 'Иззранные пользователя'
