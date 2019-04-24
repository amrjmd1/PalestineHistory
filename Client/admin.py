from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'category', 'is_active')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'id', 'category')
    list_per_page = 25


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_manager', 'is_active')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'id')
    list_per_page = 25


class UserAgentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'logout', 'manage', 'start_session')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'id')
    list_filter = ('manage', 'logout')
    list_per_page = 25


class LoginAttemptsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'name', 'date', 'manage')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_filter = ('manage',)
    list_per_page = 25


class VerifyEmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_time', 'random_number')
    list_display_links = ('id', 'client')
    search_fields = ('client', 'id')
    list_per_page = 25


admin.site.register(Client, ClientAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(UserAgents, UserAgentsAdmin)
admin.site.register(LoginAttempts, LoginAttemptsAdmin)
admin.site.register(VerifyEmail, VerifyEmailAdmin)
