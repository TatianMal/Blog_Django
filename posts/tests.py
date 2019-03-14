from uuid import uuid4
from datetime import timedelta

from django.utils import timezone
from django.test import TestCase
from .models import get_path_to_upload, Post, ImagesFromPost


class ImageFromPostTests(TestCase):

    def test_get_path_to_upload_return_correct_path(self):
        """get_path_to_upload() must to return path, witch matches post_idPost/name.ext"""
        post = Post(title='test', date=timezone.now(), active=False, content="test")
        post.save()
        correct_path = 'post_' + str(post.id)
        image = ImagesFromPost(post=post)
        created_path = get_path_to_upload(image, 'SdjaiGyAKh8.jpg')
        check_part_path = created_path.split('/')[0]
        self.assertEqual(correct_path, check_part_path)


