from django.test import TestCase
from django.urls import reverse


class PostListViewTests(TestCase):
    def test_assignment09_renders_at_root(self):
        response = self.client.get(reverse('assignment09'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '실습 과제 09')
        self.assertContains(response, '광야 - 이육사')
        self.assertContains(response, 'section / aside / footer')

    def test_post_list_renders_custom_template(self):
        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "KHU's blog")
        self.assertContains(response, 'My first post')
        self.assertContains(response, 'My second post')
