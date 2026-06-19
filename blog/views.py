import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def assignment09(request):
    return render(request, 'blog/assignment09.html', {})


def js_test(request):
    return render(request, 'blog/js_test.html', {})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def api_post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('-published_date', '-created_date')[:20]
        return JsonResponse({
            'count': posts.count(),
            'results': [serialize_post(request, post) for post in posts],
        })

    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON body.'}, status=400)

    author = resolve_author(payload.get('author'))
    title = payload.get('title') or '안드로이드-REST API 테스트'
    text = payload.get('text') or '안드로이드로 작성된 REST API 테스트 입력입니다.'
    created_date = parse_datetime(payload.get('created_date') or '') or timezone.now()
    published_date = parse_datetime(payload.get('published_date') or '') or timezone.now()

    post = Post.objects.create(
        author=author,
        title=title,
        text=text,
        created_date=created_date,
        published_date=published_date,
    )
    return JsonResponse(serialize_post(request, post), status=201)


def resolve_author(author_id):
    User = get_user_model()
    if author_id:
        try:
            return User.objects.get(pk=author_id)
        except (TypeError, ValueError, User.DoesNotExist):
            pass

    author, _ = User.objects.get_or_create(username='ystc1247')
    return author


def serialize_post(request, post):
    image_url = post.image.url if post.image else ''
    if image_url:
        image_url = request.build_absolute_uri(image_url)

    return {
        'id': post.pk,
        'author': post.author_id,
        'title': post.title,
        'text': post.text,
        'created_date': post.created_date.isoformat() if post.created_date else None,
        'published_date': post.published_date.isoformat() if post.published_date else None,
        'image': image_url,
    }
