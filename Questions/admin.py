from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'category')
    list_display_links = ('id', 'question')
    search_fields = ('question', 'id', 'category')
    list_per_page = 25


admin.site.register(ExcelFiles)
admin.site.register(Question, QuestionAdmin)
