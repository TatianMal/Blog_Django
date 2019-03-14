from datetime import timedelta
from uuid import uuid4

from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Post(models.Model):
    active = models.BooleanField(null=True)
    date = models.DateTimeField('Date published')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) < self.date

    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


def get_path_to_upload(instance, filename):
    ext = filename.split('.')[-1]  # may loaded other ext?
    filename = "%s.%s" % (uuid4(), ext)
    return 'post_{0}/{1}'.format(instance.post.id, filename)


def get_deleted_user():  # static method from User class?
    del_user = get_user_model().objects.get(name="Deleted user")
    return del_user.id


class ImagesFromPost(models.Model):
    post = models.ForeignKey(Post, on_delete='CASCADE')
    image = models.ImageField(upload_to=get_path_to_upload)


class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete='CASCADE')
    id_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=get_deleted_user,
    )
    date = models.DateTimeField('Date published')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
