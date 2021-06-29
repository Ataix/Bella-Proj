from django.contrib.auth import get_user_model
from django.db import models

ProfileUser = get_user_model()

Product = 'Product'


class OrderItem(models.Model):
    """
    Model that characterises each item of order
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='Товар в заказе'
    )
    quantity = models.IntegerField(related_name='Количество товаров')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, related_name='Цена товара'
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
    user = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE,
        related_name='Заказщик', null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, related_name='Время создания заказа'
    )
    customer_first_name = models.CharField(
        max_length=50, related_name='Имя заказщика'
    )
    customer_last_name = models.CharField(
        max_length=50, related_name='Фамилия заказщика'
    )
    customer_city = models.CharField(
        max_length=50, related_name='Город поставки'
    )
    customer_country = models.CharField(
        max_length=50, related_name='Страна поставки'
    )
    customer_phone = models.CharField(
        max_length=20, related_name='Телефон заказщика'
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, related_name='Итоговая цена заказа'
    )
    items = models.ManyToManyField(OrderItem, related_name='Товары заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user} {self.items}'
