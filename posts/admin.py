from django.contrib import admin
from .models import Post, ImagesFromPost, Comment

admin.site.register(Post)
admin.site.register(ImagesFromPost)
admin.site.register(Comment)
