from rest_framework import serializers

from apps.product.models import Category, Product, Wish
from apps.product.utils import ImageUrl


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'season',
            'parent'
        )


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = (
            'user',
            'product'
        )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user
        wish = Wish.objects.create(**validated_data)
        return wish

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.customer.username
        return representation


class ProductListSerializer(ImageUrl, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'size',
            'length',
            'discount',
            'create_date',
            'is_popular',
            'categories',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_img_url(instance)
        representation['categories'] = CategorySerializer(
            instance.categories.all(), many=True
        ).data
        return representation


class ProductRetrieveSerializer(ImageUrl, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'article',
            'quantity',
            'price',
            'description',
            'size',
            'structure',
            'length',
            'style',
            'discount',
            'is_popular',
            'categories',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_img_url(instance)
        representation['categories'] = CategorySerializer(
            instance.categories.all(), many=True
        ).data
        return representation
