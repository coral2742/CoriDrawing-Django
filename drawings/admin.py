from django.contrib import admin
from .models import DrawingItem, DrawingCategory
# Register your models here.


@admin.register(DrawingItem)
class DrawingItemAdmin(admin.ModelAdmin):
    list_display = ("title","type",)


@admin.register(DrawingCategory)
class DrawingCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)