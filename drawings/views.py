from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404

from .models import DrawingItem, DrawingCategory
from django.conf import settings

class Index(ListView):
    template_name = "drawings/index.html"
    model = DrawingCategory
    context_object_name = "categories"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = DrawingCategory.objects.all().order_by('priority')
        context["CLOUDINARY_URL_MEDIA"] = settings.CLOUDINARY_URL_MEDIA
        return context


class DrawingListView(ListView):
    template_name = "drawings/category.html"
    model = DrawingItem
    context_object_name = "draws"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_short_title = self.kwargs["short_title"]
        category = get_object_or_404(DrawingCategory, short_title__iexact=category_short_title)
        context['category'] = category
        return context

    def get_queryset(self):
        category_short_title = self.kwargs["short_title"]
        queryset = DrawingItem.objects.filter(type__short_title__iexact=category_short_title).order_by('priority')
        return queryset