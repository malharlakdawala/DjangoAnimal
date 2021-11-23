from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    address=models.CharField(max_length=255)