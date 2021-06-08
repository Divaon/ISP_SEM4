from blog.forms import *
from django.test import TestCase

class TestForms(TestCase):
    # checking when form was not initialized with data
    def test_tag_form_no_data(self):
        form = TagForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_post_form_no_data(self):
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)