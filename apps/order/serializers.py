from rest_framework import serializers

from apps.order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'product', 'quantity', 'price'
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'user', 'created_at', 'customer_first_name', 'customer_last_name',
            'customer_city', 'customer_country', 'customer_phone', 'total',
            'items'
        )


class OrderUpdateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'customer_city', 'customer_country', 'items', 'total'
        )
