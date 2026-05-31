from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def create_sample_posts(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('blog', 'Post')

    author, _ = User.objects.get_or_create(
        username='ystc1247',
        defaults={
            'email': 'ystc1247@example.com',
            'is_staff': True,
            'is_superuser': True,
        },
    )

    now = timezone.now()
    samples = [
        (
            'Django template practice',
            'Ch17 실습: 모델의 데이터를 템플릿으로 전달하고, for loop와 템플릿 태그를 사용합니다.\n'
            '게시글 제목을 클릭하면 상세 페이지로 이동합니다.',
        ),
        (
            'CSS styling with static files',
            'Bootstrap, Google Fonts, static CSS 파일을 연결하여 블로그 화면을 꾸몄습니다.\n'
            'base.html을 사용해 공통 레이아웃도 재사용합니다.',
        ),
    ]

    for index, (title, text) in enumerate(samples):
        Post.objects.get_or_create(
            title=title,
            defaults={
                'author': author,
                'text': text,
                'created_date': now,
                'published_date': now - timedelta(minutes=index),
            },
        )


def remove_sample_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(
        title__in=[
            'Django template practice',
            'CSS styling with static files',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_posts, remove_sample_posts),
    ]
