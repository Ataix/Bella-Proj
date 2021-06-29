from django.contrib import admin

from apps.order.models import OrderItem, Order


@admin.register(OrderItem)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Order)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
