from django.db import models
from django.utils import timezone
# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=timezone.now())
    created_in_country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='films_created_in')
    available_in_countries = models.ManyToManyField('Country', related_name='films_available_in')
    categories = models.ManyToManyField('Category')
    directors = models.ManyToManyField('Director')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Countries'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.title()
