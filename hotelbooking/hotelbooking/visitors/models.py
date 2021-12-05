from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, upload_to='profile_pics/')

    def pic(self):
        if self.image:

            return self.image.url
        else:
            return 'https://bootdey.com/img/Content/avatar/avatar6.png'


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    complete_percent = models.IntegerField(default=0)

    def div_color(self):
        if 20 > self.complete_percent:
            return 'danger'
        if 40 > self.complete_percent > 20:
            return 'warning'
        if 60 > self.complete_percent > 40:
            return 'info'
        if 80 > self.complete_percent > 60:
            return 'primary'
        else:
            return 'success'
