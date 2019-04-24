from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    list_per_page = 25


admin.site.register(Event, EventAdmin)
