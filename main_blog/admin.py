from django.contrib import admin

from .models import Post, ImagesFromPost

admin.site.register(Post)
admin.site.register(ImagesFromPost)