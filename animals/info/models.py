from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    #age=models.PositiveIntegerField()

class Family(models.Model):
    name=models.CharField(max_length=100)
    members=models.IntegerField()

