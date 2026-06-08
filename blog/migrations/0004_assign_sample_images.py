from django.db import migrations


def assign_sample_images(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    image_by_title = {
        'Django template practice': 'intruder_image/2026/06/08/django_template.png',
        'CSS styling with static files': 'intruder_image/2026/06/08/rest_image_blog.png',
    }
    for title, image in image_by_title.items():
        Post.objects.filter(title=title).update(image=image)


def reset_sample_images(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(
        title__in=[
            'Django template practice',
            'CSS styling with static files',
        ]
    ).update(image='intruder_image/default_error.png')


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.RunPython(assign_sample_images, reset_sample_images),
    ]
