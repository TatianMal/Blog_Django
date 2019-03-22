from django.contrib import admin
from .models import Post, ImagesFromPost, Comment


class ImagesInline(admin.StackedInline):
    model = ImagesFromPost
    extra = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ['title', 'published', 'date']
    list_filter = ['date', 'published']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(ImagesFromPost)
admin.site.register(Comment)


