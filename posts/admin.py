from django.contrib import admin
from .models import Post, ImagesFromPost, Comment, Category


class CategoriesInline(admin.TabularInline):
    model = Category.posts.through


class ImagesInline(admin.StackedInline):
    model = ImagesFromPost
    extra = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, CategoriesInline]
    list_display = ['title', 'published', 'date']
    list_filter = ['date', 'published']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline]
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(ImagesFromPost)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)


