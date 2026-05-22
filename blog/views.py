from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def assignment09(request):
    return render(request, 'blog/assignment09.html', {})
