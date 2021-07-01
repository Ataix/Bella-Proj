from django.contrib import admin

from apps.order.models import OrderItem, Order


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'created_at', 'customer_first_name', 'customer_last_name',
        'customer_city', 'customer_country', 'customer_phone', 'total', 'items'
    )
