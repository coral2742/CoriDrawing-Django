from django.db import models

# Create your models here.

class DrawingCategory(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    short_title = models.CharField("Short title", max_length=200)
    description = models.TextField("Description", max_length=500, blank=True)
    image = models.ImageField(upload_to="images", default="media/images/Error404.jpg")
    priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

class DrawingItem(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    type = models.ForeignKey(DrawingCategory, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(default=0)
    description = models.TextField("Description", max_length=500, blank=True)
    image = models.ImageField(upload_to="images", default="media/images/Error404.jpg")
    video = models.FileField(upload_to="videos", blank=True)

    def video_url(self):
        if self.video:
            return f"https://res.cloudinary.com/dkny1x3tp/video/upload/{self.video.name}"
        return None

    def __str__(self):
        return f"{self.title}"