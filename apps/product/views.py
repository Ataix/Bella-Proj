from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,CreateAPIView, DestroyAPIView
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSetMixin

from apps.product.models import Category, Product, Wish
from apps.product.serializers import (
    CategorySerializer, ProductListSerializer, ProductRetrieveSerializer,
    WishSerializer
)
from apps.product.service import WishListService
from apps.product.utils import IsOwnerWish


class BellaPagination(PageNumberPagination):
    page_size = 5


class CategoryListView(ListAPIView):
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
    permission_classes = [IsAuthenticated]


class WishViewSet(ViewSetMixin,
                  RetrieveAPIView,
                  CreateAPIView,
                  DestroyAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = [IsOwnerWish]
