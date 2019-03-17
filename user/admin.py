from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'phone',
        'qq',
        'is_active',
        'is_staff',
        'last_login',
        'date_joined'
    ]
    list_filter = [
        'is_active',
        'is_staff',
        'date_joined'
    ]
    search_fields = [
        'email',
        'username',
        'phone',
        'qq',
    ]


@admin.register(models.ForgetPassword)
class ForgetPassword(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'created_datetime'
    ]
    list_filter = [
        'created_datetime'
    ]
    search_fields = [
        'email'
    ]


@admin.register(models.SigninUserInfo)
class SiginUserInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'phone',
        'qq',
        'date_joined'
    ]
    list_filter = [
        'date_joined'
    ]
    search_fields = [
        'email',
        'username',
        'phone',
        'qq',
    ]
