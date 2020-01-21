from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class BasicModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Slider(BasicModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = ProcessedImageField(upload_to='sliders', processors=[
                                ResizeToFill(1920, 1080)], format='JPEG', options={'quality': 60})
    slider_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Service(BasicModel):

    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    image = ProcessedImageField(upload_to='services', processors=[
                                ResizeToFill(100, 100)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.name
