from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),  # get with filter
    path(r'post/create', views.add_comment, name='comment'),  # post
    path(r'post/<int:post_id>/', views.detail_post, name='detail'),  # get
    path(r'post/<int:post_id>/preview', views.add_comment, name='comment'),  # get??
    path(r'post/<int:post_id>/edit', views.add_comment, name='comment'),  # patch
]