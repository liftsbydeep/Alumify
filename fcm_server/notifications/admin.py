from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'phone', 'email', 'fcm_token')
    search_fields = ('name', 'email')
