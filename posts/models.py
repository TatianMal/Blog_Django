from django.db import models
from django.conf import settings


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
    pass
    # TODO: write function to create path images (id_post directory)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.id, filename)


class ImagesFromPost(models.Model):
    id_post = models.ForeignKey(Post, on_delete='CASCADE')
    image = models.ImageField(upload_to=get_path_to_upload)


class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete='CASCADE')
    id_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=1,
        #     TODO: create function, where set "deleted" user to mark same users
    )
    date = models.DateTimeField('Date published')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
