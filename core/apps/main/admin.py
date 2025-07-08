from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from decimal import Decimal

from constance import settings, forms as constance_forms
from constance.admin import ConstanceAdmin, Config
from django.contrib import admin
from django.forms import fields
from unfold import widgets
from unfold.admin import ModelAdmin, TabularInline

from . import models


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


NUMERIC_WIDGET = widgets.UnfoldAdminTextInputWidget(attrs={'size': 10})

INTEGER_LIKE = (fields.IntegerField, {'widget': NUMERIC_WIDGET})
STRING_LIKE = (
    fields.CharField,
    {
        'widget': widgets.UnfoldAdminTextareaWidget(attrs={'rows': 3}),
        'required': False,
    },
)

FIELDS = {
    bool: (fields.BooleanField, {'required': False, 'widget': widgets.UnfoldBooleanSwitchWidget}),
    int: INTEGER_LIKE,
    Decimal: (fields.DecimalField, {'widget': NUMERIC_WIDGET}),
    str: STRING_LIKE,
    datetime: (fields.SplitDateTimeField, {'widget': widgets.UnfoldAdminSplitDateTimeWidget}),
    timedelta: (fields.DurationField, {'widget': widgets.UnfoldAdminTextInputWidget}),
    date: (fields.DateField, {'widget': widgets.UnfoldAdminDateWidget}),
    time: (fields.TimeField, {'widget': widgets.UnfoldAdminTimeWidget}),
    float: (fields.FloatField, {'widget': NUMERIC_WIDGET}),
}

# Don't call parse_additional_fields again - constance calls it before us.
FIELDS.update(settings.ADDITIONAL_FIELDS)

# Monkey patch constance module to use our custom fields.
constance_forms.FIELDS = FIELDS


class UnfoldConstanceForm(constance_forms.ConstanceForm):
    pass


if admin.site.is_registered(ConstanceAdmin):
    admin.site.unregister(ConstanceAdmin)

if admin.site.is_registered(Config):
    admin.site.unregister([Config])


class CustomConstanceAdmin(ConstanceAdmin):
    change_list_template = 'unfold/constance/index.html'
    change_list_form = UnfoldConstanceForm


admin.site.register([Config], CustomConstanceAdmin)
