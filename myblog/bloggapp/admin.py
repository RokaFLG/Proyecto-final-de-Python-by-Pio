

from django.contrib import admin
from .models import Blog, Page

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'date')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'subtitle': ('title',)}

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
