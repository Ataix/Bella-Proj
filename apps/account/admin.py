from django.contrib import admin
from django.contrib.auth import get_user_model


ProfileUser = get_user_model()


@admin.register(ProfileUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
