from django.contrib import admin

from . import models


@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
