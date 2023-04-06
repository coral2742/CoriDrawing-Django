from django.db import models

# Create your models here.

class DrawingCategory(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    short_title = models.CharField("Short title", max_length=200)
    description = models.TextField("Description", max_length=500, blank=True)
    image = models.ImageField(upload_to="images", default="images/Error404.jpg")
    priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

class DrawingItem(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    type = models.ForeignKey(DrawingCategory, on_delete=models.CASCADE)
    description = models.TextField("Description", max_length=500, blank=True)
    image = models.ImageField(upload_to="images", default="images/Error404.jpg")
    video = models.FileField(upload_to="videos", blank=True)

    def __str__(self):
        return f"{self.title}"