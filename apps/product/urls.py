from django.urls import path

from apps.product.views import (
    CategoryListView, ProductListView, ProductRetrieveView, WishListView,
    WishViewSet
)

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('', ProductListView.as_view()),
    path('product/<int:pk>/', ProductRetrieveView.as_view()),
    path('wish_list/', WishListView.as_view()),
    path(
        'wish/', WishViewSet.as_view({
            'get': 'retrieve',
            'post': 'create',
            'delete': 'destroy'
        })),
]
