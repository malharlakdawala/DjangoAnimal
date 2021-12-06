from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum_post(models.Model):
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    forum_post_author = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Comment_post(models.Model):
    #forum = models.ForeignKey(Forum_post, blank=True, on_delete=models.CASCADE, related_name='comments')
    forum = models.ForeignKey(Forum_post, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    comment_author = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.forum)
