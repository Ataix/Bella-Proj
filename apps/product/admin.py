from django.contrib import admin

from .models import Image, Category, Product, Colour, Wish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'season',
        'parent'
    )


class ImgInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImgInline
    ]
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
        'categories',
    )

    def categories(self, instance):
        return instance.product.categories.category


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
