from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Post


class PostListViewTests(TestCase):
    def test_assignment09_renders_at_root(self):
        response = self.client.get(reverse('assignment09'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '실습 과제 09')
        self.assertContains(response, '광야 - 이육사')
        self.assertContains(response, 'section / aside / footer')

    def test_js_test_renders_number_guessing_game(self):
        response = self.client.get(reverse('js_test'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Number guessing game')
        self.assertContains(response, 'Math.floor(Math.random() * 100) + 1')
        self.assertContains(response, "document.querySelector('.lowOrHi')")
        self.assertContains(response, "guessSubmit.addEventListener('click', checkGuess)")

    def test_post_list_renders_ch17_blog_posts(self):
        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Web Service programming blog')
        self.assertContains(response, 'Django template practice')
        self.assertContains(response, 'CSS styling with static files')
        self.assertContains(response, 'intruder-image-list')
        self.assertContains(response, '/media/intruder_image/')

    def test_post_detail_renders_post_content(self):
        author = get_user_model().objects.get(username='ystc1247')
        post = Post.objects.create(
            author=author,
            title='Detail test post',
            text='This post checks the detail template.',
            published_date=timezone.now(),
        )

        response = self.client.get(reverse('post_detail', kwargs={'pk': post.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detail test post')
        self.assertContains(response, 'This post checks the detail template.')
        self.assertContains(response, 'intruder-image-detail')
