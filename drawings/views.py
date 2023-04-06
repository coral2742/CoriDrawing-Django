from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import DrawingItem, DrawingCategory

class Index(ListView):
    template_name = "drawings/index.html"
    model = DrawingCategory
    context_object_name = "categories"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = DrawingCategory.objects.all()
        return context


class DrawingListView(ListView):
    template_name = "drawings/category.html"
    model = DrawingItem
    context_object_name = "draws"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_title = self.kwargs["title"]
        category = get_object_or_404(DrawingCategory, title__iexact=category_title)
        context['category'] = category
        return context

    def get_queryset(self):
        category_title = self.kwargs["title"]
        queryset = DrawingItem.objects.filter(type__title__iexact=category_title)
        return queryset