from django.contrib import admin
from .models import Ad, AdImage

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']

@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):
    list_display = [
        'ad',
        'image',
    ]
