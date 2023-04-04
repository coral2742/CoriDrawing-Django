from django.shortcuts import render
from django.views.generic import ListView
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


class CategoriesView(ListView):
    model = DrawingCategory

    template_name = "drawings/category.html"
    model = DrawingCategory
    context_object_name = "category"

    def get_queryset(self):
        request_id = int(self.kwargs["pk"])
        queryset = get_object_or_404(DrawingCategory, id=request_id)
        return queryset