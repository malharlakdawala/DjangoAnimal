from django.db import models
from datetime import datetime

# Create your models here.
class GifModel(models.Model):
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    uploader_name=models.CharField(max_length=50)
    created_at =models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f'{self.title}'

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    gifs=models.ManyToManyField(GifModel, related_name='categories', blank=True)

    def __str__(self):
        return f'Category {self.name}'

