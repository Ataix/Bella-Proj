from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.product.models import Category, Product, Wish
from apps.product.serializers import (
    CategorySerializer, ProductListSerializer, ProductRetrieveSerializer,
    WishSerializer
)
from apps.product.service import WishListService


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer


class WishListView(WishListService):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
