from datetime import timedelta
from uuid import uuid4

from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Post(models.Model):
    published = models.BooleanField(default=False)
    date = models.DateTimeField('Date published')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


def get_path_to_upload(instance, filename):
    ext = filename.split('.')[-1]  # may loaded other ext?
    filename = "%s.%s" % (uuid4(), ext)
    return 'post_{0}/{1}'.format(instance.post.id, filename)


def get_deleted_user():
    del_user, created = get_user_model().objects.get_or_create(username="Deleted user", password='deletedUser')
    return del_user.id


class ImagesFromPost(models.Model):
    post = models.ForeignKey(Post, on_delete='CASCADE')
    image = models.ImageField(upload_to=get_path_to_upload)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete='CASCADE')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=get_deleted_user,
    )
    date = models.DateTimeField('Date published')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name + " " + self.post.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Category(models.Model):
    posts = models.ManyToManyField(Post)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
