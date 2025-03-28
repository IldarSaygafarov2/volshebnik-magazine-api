from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.Catalog)
class CatalogAdmin(ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_display_links = ['pk', 'name']


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['pk', 'name', 'catalog']
    list_display_links = ['pk', 'name']
    list_editable = ['catalog']
    search_fields = ['name']
    list_filter = ['catalog']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.PublishingHouse)
class PublishingHouseAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Series)
class SeriesAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    list_display = ['pk', 'name', 'price', 'in_stock', 'barcode']
    list_display_links = ['pk', 'name']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['created_at']
    search_fields = ['name']
