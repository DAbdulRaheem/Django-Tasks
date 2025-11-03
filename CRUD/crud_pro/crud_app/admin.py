from django.contrib import admin

# Register your models here.
from .models import FavoriteItem

@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
