from django.contrib import admin

from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_at', 'views_count')
    list_filter = ('status', 'published_at')
    search_fields = ('title', 'content')
    readonly_fields = ('views_count',)
    ordering = ('-published_at',)