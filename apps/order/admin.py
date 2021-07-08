from django.contrib import admin

from apps.order.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = Order.items.through
    fields = ['product', 'quantity', 'price']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = (
        'customer_user', 'created_at', 'customer_first_name',
        'customer_last_name', 'customer_city', 'customer_country',
        'customer_phone', 'total'
    )
