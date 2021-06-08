from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *

class TestUrls(SimpleTestCase):
    def test_posts_list_url_is_resolved(self):
        url = reverse('posts_list_url')
        self.assertEquals(resolve(url).func, posts_list)

    def test_post_create_url_is_resolved(self):
        url = reverse('post_create_url')
        self.assertEquals(resolve(url).func.view_class, PostCreate)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail_url', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_post_update_url_is_resolved(self):
        url = reverse('post_update_url', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostUpdate)

    def test_post_delete_url_is_resolved(self):
        url = reverse('post_delete_url', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDelete)

    def test_tags_list_url_is_resolved(self):
        url = reverse('tags_list_url')
        self.assertEquals(resolve(url).func, tags_list)

    def test_tag_create_url_is_resolved(self):
        url = reverse('tag_create_url')
        self.assertEquals(resolve(url).func.view_class, TagCreate)

    def test_tag_detail_url_is_resolved(self):
        url = reverse('tag_detail_url', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, TagDetail)

    def test_tag_update_url_is_resolved(self):
        url = reverse('tag_update_url', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, TagUpdate)

    def test_tag_delete_url_is_resolved(self):
        url = reverse('tag_delete_url', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, TagDelete)

    def test_login_url_is_resolved(self):
        url = reverse('login_url')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_register_url_is_resolved(self):
        url = reverse('register_url')
        self.assertEquals(resolve(url).func.view_class, RegisterView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout_url')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_profile_url_is_resolved(self):
        url = reverse('profile_url')
        self.assertEquals(resolve(url).func.view_class, ProfileView)


