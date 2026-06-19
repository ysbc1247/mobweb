from django.urls import path

from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('upload/', views.photo_upload, name='photo_upload'),
    path('html5/', views.assignment09, name='assignment09'),
    path('js-test/', views.js_test, name='js_test'),
    path('api_root/Post/', views.api_post_collection, name='api_post_collection'),
]
