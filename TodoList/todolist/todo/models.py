from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Todo(models.Model):
    title=models.CharField(max_length=50)
    details=models.TextField ()
    has_been_done =models.BooleanField(default=False)
    date_creation =models.DateTimeField(auto_now_add=True, blank=True)
    date_completion =models.DateTimeField(blank=True, null=True)
    deadline_date =models.DateTimeField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering=["title"]

