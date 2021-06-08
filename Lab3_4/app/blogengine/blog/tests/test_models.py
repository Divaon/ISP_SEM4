from django.test import TestCase
from blog.models import *

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        tag1 = Tag.objects.create(title='super tag1', slug='some-slug-1')
        tag1.save()
        tag2 = Tag.objects.create(title='super tag2', slug='some-slug-2')
        tag2.save()

        user = User()
        user.username = "Username"
        user.save()

        post = Post()
        post.title = "Post title"
        post.body = "some body and some text inside it..."
        post.user = user
        post.save()
        post.tags.add(tag1, tag2)

    def test_tag_is_assigned_slug_on_creation(self):
        tag = Tag.objects.get(id=1)
        self.assertEquals(tag.slug, 'some-slug-1')

    def test_tag_absolute_url(self):
        tag = Tag.objects.get(id=1)
        self.assertEquals(tag.get_absolute_url(), '/blog/tag/some-slug-1/')

    def test_post_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/blog/post/' + post.slug + '/')