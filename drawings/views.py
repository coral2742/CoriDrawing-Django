from django.shortcuts import render
from django.views.generic import ListView

from .models import DrawingItem

class Index(ListView):
    template_name = "drawings/index.html"
    model = DrawingItem
    context_object_name = "drawings"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["drawings"] = DrawingItem.objects.all()
        return context

