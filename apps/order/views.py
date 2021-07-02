from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView
)

from apps.order.models import Order
from apps.order.serializers import OrderSerializer, OrderUpdateSerializer
from apps.order.service import OrderListService


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(OrderListService):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
