from django.shortcuts import render

class Index(ListView):
    template_name = "drawings/index.html"
    model = DrawingItem
    context_object_name = "drawings"

    def get_context_data(self, **kwargs):
        context = DrawingItem.objects.all()
        return context
