from django.contrib.auth import get_user_model
import json

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

    def test_android_api_creates_post_with_default_image(self):
        payload = {
            'author': 1,
            'title': '안드로이드-REST API 테스트',
            'text': '안드로이드로 작성된 REST API 테스트 입력입니다.',
            'created_date': '2024-06-03T18:34:00+09:00',
            'published_date': '2024-06-03T18:34:00+09:00',
        }

        response = self.client.post(
            reverse('api_post_collection'),
            data=json.dumps(payload),
            content_type='application/json',
            HTTP_AUTHORIZATION='JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd',
        )

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['title'], '안드로이드-REST API 테스트')
        self.assertIn('/media/intruder_image/default_error.png', data['image'])
        self.assertTrue(Post.objects.filter(title='안드로이드-REST API 테스트').exists())
