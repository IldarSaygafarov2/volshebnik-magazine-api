from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(models.Subcategory)
class SubcategoryAdmin(ModelAdmin):
    list_display = ['pk', 'name', 'slug', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['pk', 'name']
    list_filter = ['category', 'created_at']
    list_editable = ['category']
    search_fields = ['name']


@admin.register(models.PublishingHouse)
class PublishingHouseAdmin(ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created_at']
    search_fields = ['name']

# @admin.register(models.ProductVariant)
# class ProductVariantAdmin(ModelAdmin):
#     list_display = ['pk', 'name', 'category', 'subcategory']
#     list_display_links = ['pk', 'name']
#     list_editable = ['category', 'subcategory']
#     list_filter = ['category', 'subcategory', 'created_at']
#     prepopulated_fields = {'slug': ('name',)}
#     search_fields = ['name']