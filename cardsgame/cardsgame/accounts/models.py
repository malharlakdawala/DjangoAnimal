from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

class Starwars_people(models.Model):
    name = models.CharField(max_length=50)
    height = models.FloatField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.CharField(max_length=50, null=True)
