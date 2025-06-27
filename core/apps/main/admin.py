from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin, TabularInline


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]
    list_filter = ["created_at"]
    search_fields = ["name"]


@admin.register(models.Subcategory)
class SubcategoryAdmin(ModelAdmin):
    list_display = ["pk", "name", "slug", "category"]
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ["pk", "name"]
    list_filter = ["category", "created_at"]
    list_editable = ["category"]
    search_fields = ["name"]


@admin.register(models.PublishingHouse)
class PublishingHouseAdmin(ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created_at"]
    search_fields = ["name"]


@admin.register(models.CategoryAge)
class CategoryAgeAdmin(ModelAdmin):
    pass


class ProductImageInline(TabularInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    list_display = [
        "barcode",
        "title",
        "price",
        "publisher",
        "main_category",
        "subcategory",
    ]
    list_display_links = ["barcode", "title"]
    list_editable = ["publisher", "main_category", "subcategory", "price"]
    list_filter = [
        "publisher",
        "main_category",
        "subcategory",
        "is_on_sale",
        "is_new",
        "is_bestseller",
    ]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "barcode"]
    inlines = [ProductImageInline]


@admin.register(models.Slider)
class SliderAdmin(ModelAdmin):
    pass
