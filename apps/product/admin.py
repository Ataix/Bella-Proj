from django.contrib import admin

from apps.product.models import Image, Category, Product, Colour, Wish


class ImgInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


class ProductFull(admin.ModelAdmin):
    inlines = [
        ImgInline
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'season',
        'parent'
    )


@admin.register(Product, ProductFull)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
        'categories'
    )


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name'
    )


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product'
    )
