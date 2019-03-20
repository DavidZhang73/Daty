from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'user',
        'email'
    ]
    search_fields = [
        'name',
        'name',
        'email',
    ]


@admin.register(models.UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'type',
        'creator',
        'created_datetime',
        'last_modified_datetime'
    ]
    list_filter = [
        'type'
    ]
    search_fields = [
        'name',
        'type',
    ]
