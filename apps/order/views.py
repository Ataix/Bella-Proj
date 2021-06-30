from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from apps.order.filters import OrderFilter
from apps.order.models import Order
from apps.order.serializers import OrderSerializer, OrderUpdateSerializer
from apps.order.service import OrderCreateService


class OrderCreateView(OrderCreateService, CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_class = OrderFilter
    filter_backends = [DjangoFilterBackend]


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_class = OrderFilter
    filter_backends = [DjangoFilterBackend]


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [IsAuthenticated]
    filter_class = OrderFilter
    filter_backends = [DjangoFilterBackend]
