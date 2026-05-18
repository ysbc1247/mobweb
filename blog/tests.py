from django.test import TestCase
from django.urls import reverse


class PostListViewTests(TestCase):
    def test_post_list_renders_custom_template(self):
        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "KHU's blog")
        self.assertContains(response, 'My first post')
        self.assertContains(response, 'My second post')
