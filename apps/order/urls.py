from django.urls import path

from apps.order.views import (
    OrderCreateView, OrderListView, OrderDetailView, OrderUpdateView
)

urlpatterns = [
    path('order_create/', OrderCreateView.as_view()),
    path('orders/', OrderListView.as_view()),
    path('order/<int:pk>/', OrderDetailView.as_view()),
    path('order_update/<int:pk>/', OrderUpdateView.as_view())
]
