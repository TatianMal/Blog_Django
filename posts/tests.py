from uuid import uuid4
from datetime import timedelta

from django.utils import timezone
from django.test import TestCase
from .models import get_path_to_upload, Post, ImagesFromPost, Comment
from django.contrib.auth import get_user_model


class ImageFromPostTests(TestCase):

    def test_get_path_to_upload_return_correct_path(self):
        """get_path_to_upload() must to return path, which matches post_idPost/name.ext"""
        post = Post(title='test', date=timezone.now(), active=False, content="test")
        post.save()
        correct_path = 'post_' + str(post.id)
        image = ImagesFromPost(post=post)
        created_path = get_path_to_upload(image, '123.jpg')
        check_part_path = created_path.split('/')[0]
        self.assertEqual(correct_path, check_part_path)


class CommentTests(TestCase):

    def test_get_deleted_user_for_comment(self):
        """added comment without new user must have deleted user as author"""
        post = Post(title='test', date=timezone.now(), active=False, content="test")
        post.save()
        deleted_user, created = get_user_model().objects.get_or_create(username='Deleted user', password='deletedUser')
        tested_comment = Comment(post=post, date=timezone.now(), content='some content')
        self.assertEqual(tested_comment.author.id, deleted_user.id)

        # TODO: test to check does comment take delete user after user deletion (deactivation?)
