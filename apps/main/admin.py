from django.contrib import admin

from apps.main.models import (
    Delivery, AboutUs, Contact, WaysOfPayment, QuestionAndAnswer,
    ProductReturn, Requisite, PublicOffer, HowToMakeOrder, News
)


@admin.register(Delivery)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('upward_text', 'upward_img', 'bottom_text', 'bottom_img')


@admin.register(AboutUs)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'left_up_img', 'right_down_img', 'upward_text', 'bottom_text'
    )


@admin.register(Contact)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number', 'email', 'address', 'odnoklassniki', 'vkontakte',
        'instagram', 'facebook'
    )


@admin.register(WaysOfPayment)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'text_about_payment', 'requisite_1', 'requisite_2', 'requisite_3'
    )


@admin.register(QuestionAndAnswer)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'upward_question', 'upward_answer', 'bottom_question', 'bottom_answer'
    )


@admin.register(ProductReturn)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('upward_text', 'bottom_text')


@admin.register(Requisite)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('requisite_1', 'requisite_2', 'requisite_3')


@admin.register(PublicOffer)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('upward_text', 'bottom_text')


@admin.register(HowToMakeOrder)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('upward_text', 'upward_img', 'bottom_img', 'bottom_text')


@admin.register(News)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'description', 'image')
