from django.db import models
from django.conf import settings
from accounts.models import User

import uuid


class Post(models.Model):
    active = models.BooleanField(null=True)
    date = models.DateTimeField('Date published')
    title = models.CharField(max_length=100)
    content = models.TextField()
    # images = models.ForeignKey()
    # comments = models.ForeignKey()

    def __str__(self):
        return self.title


def get_path_to_upload(instance, filename):
    ext = filename.split('.')[-1]  # may loaded other ext?
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'user_{0}/{1}'.format(instance.post.id, filename)


def get_deleted_user():  # static method from User class?
    del_user = User.objects.get(name="Deleted user")
    return del_user.id


class ImagesFromPost(models.Model):
    id_post = models.ForeignKey(Post, on_delete='CASCADE')
    image = models.ImageField(upload_to=get_path_to_upload)


class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete='CASCADE')
    id_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=get_deleted_user(),
    )
    date = models.DateTimeField('Date published')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
