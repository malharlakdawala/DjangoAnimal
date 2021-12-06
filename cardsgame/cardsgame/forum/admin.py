from django.contrib import admin
from .models import Forum_post, Comment_post
# Register your models here.
admin.site.register(Forum_post)
admin.site.register(Comment_post)
