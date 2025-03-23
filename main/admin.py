from django.contrib import admin

from . import models


@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_display_links = ['pk', 'name']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'catalog']
    list_display_links = ['pk', 'name']
    list_editable = ['catalog']
    search_fields = ['name']
    list_filter = ['catalog']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
