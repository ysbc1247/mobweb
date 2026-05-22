from django.urls import path

from . import views


urlpatterns = [
    path('', views.assignment09, name='assignment09'),
    path('django/', views.post_list, name='post_list'),
]
