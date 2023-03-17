from django.contrib import admin
from .models import DrawingItem
# Register your models here.


@admin.register(DrawingItem)
class DrawingItemAdmin(admin.ModelAdmin):
    list_display = ("title","type",)