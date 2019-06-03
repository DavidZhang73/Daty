from django.contrib import admin

from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CollectionFile)
class CollectionFileAdmin(admin.ModelAdmin):
    pass
