from django.test import TestCase, Client
from django.urls import reverse
from blog.models import *
import json
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        user = User()
        user.username = "admin"
        user.password = "admin1"
        user.save()
        self.client.force_login(user)

        self.posts_list_url = reverse('posts_list_url')
        self.tags_list_url = reverse('tags_list_url')
        self.tag_create_url = reverse('tag_create_url')
        self.post_create_url = reverse('post_create_url')
        self.login_url = reverse('login_url')
        self.register_url = reverse('register_url')

    def test_posts_list_view_GET(self):
        response = self.client.get(self.posts_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_tags_list_view_GET(self):
        response = self.client.get(self.tags_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/tags_list.html')

    def test_post_create_view_GET(self):
        response = self.client.get(self.post_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_create.html')

    def test_tag_create_view_GET(self):
        response = self.client.get(self.tag_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/tag_create.html')

    def test_login_view_GET(self):
        self.client.logout()
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/login.html')

    def test_register_view_GET(self):
        self.client.logout()
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/register.html')
