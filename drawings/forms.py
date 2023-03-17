from django import forms

from .models import DrawingItem



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



class DrawingItem(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    type = models.CharField("Type", max_length=200, default="Acuarela")
    description = models.TextField("Description", max_length=500, blank=True)
    image = models.ImageField(upload_to="images", default="images/Error404.jpg")
    video = models.FileField(upload_to="videos", blank=True)
    url_1_name = models.CharField("Url 1 name", max_length=200, blank=True)
    url_1 = models.CharField("Url 1", max_length=200, blank=True)

    def __str__(self):
        return f"{self.title}"