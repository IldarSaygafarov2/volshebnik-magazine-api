from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import NewsPost


@admin.register(NewsPost)
class NewsPostAdmin(ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk", "title"]
    list_filter = ["created_at"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
