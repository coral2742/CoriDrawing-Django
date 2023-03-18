from django import forms

from .models import DrawingItem, Categories



class DrawingItemForm(forms.ModelForm):
    class Meta:
        model = DrawingItem
        fields = ("title", "type","description", "image", "video", 
        "url_1_name", "url_1",)

        def save(self. commit=True):
            drawing = super().save(commit=False)
            if commit:
                drawing.save()
            return drawing



class DrawingCategoryForm(forms.ModelForm):
    class Meta:
        model = Cate
        fields = ("title",)

        def save(self. commit=True):
            category = super().save(commit=False)
            if commit:
                category.save()
            return category