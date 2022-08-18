from django.shortcuts import render
from django.views.generic import ListView

from .models import DrawingItem

class Index(ListView):
    template_name = "drawings/index.html"
    model = DrawingItem
    context_object_name = "drawings"
    queryset = DrawingItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
