from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_visible']
    list_display_links = ['id', 'title']
    list_editable = ['is_visible']
    list_filter = ['is_visible']
