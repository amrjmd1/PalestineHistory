from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'identity')
    list_display_links = ('id', 'identity')
    search_fields = ('title', 'id', 'identity')
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
