from django.contrib.auth import get_user_model
from django.db import models

from apps.product.models import Product

ProfileUser = get_user_model()


class OrderItem(models.Model):
    """
    Model that characterises each item of order
    """
    product = models.ManyToManyField(
        Product, verbose_name='Товар в заказе'
    )
    quantity = models.IntegerField(verbose_name='Количество товаров')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена товара'
    )

    class Meta:
        verbose_name = 'Товар заказа'
        verbose_name_plural = 'Товары заказа'

    def __str__(self):
        return f'{self.product} {self.price}'


class Order(models.Model):
    """
    Model that characterises order of each user
    """
    customer_user = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE,
        verbose_name='Заказщик', null=True, related_name='customer_user'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания заказа'
    )
    customer_first_name = models.CharField(
        max_length=50, verbose_name='Имя заказщика'
    )
    customer_last_name = models.CharField(
        max_length=50, verbose_name='Фамилия заказщика'
    )
    customer_city = models.CharField(
        max_length=50, verbose_name='Город поставки'
    )
    customer_country = models.CharField(
        max_length=50, verbose_name='Страна поставки'
    )
    customer_phone = models.CharField(
        max_length=20, verbose_name='Телефон заказщика'
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Итоговая цена заказа'
    )
    items = models.ManyToManyField(OrderItem, verbose_name='Товары заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user} {self.items}'
