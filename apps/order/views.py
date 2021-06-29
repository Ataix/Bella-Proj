from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated

from apps.order.models import Order
from apps.order.serializers import OrderSerializer
from apps.order.service import OrderCreateService


class OrderCreateView(OrderCreateService, CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
