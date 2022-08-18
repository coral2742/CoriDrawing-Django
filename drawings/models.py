from django.db import models

# Create your models here.
class DrawingItem(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    description = models.TextField("Description", max_length=500, blank=True)
    image = models.ImageField(upload_to="images", default="images/Error404.jpg")
    video = models.FileField(upload_to="videos", blank=True)
    url_1_name = models.CharField("Url 1 name", max_length=200, blank=True)
    url_1 = models.CharField("Url 1", max_length=200, blank=True)

    def __str__(self):
        return f"{self.title}"