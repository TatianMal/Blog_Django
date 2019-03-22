from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(template_name='index.html', arg='hello')),  # get with filter
    path(r'unpublished/', views.add_comment, name='comment'),
    path(r'post/create', views.add_comment, name='comment'),  # post - in that page
    path(r'post/<int:post_id>/', views.detail_post, name='detail'),  # get
    path(r'post/<int:post_id>/preview', views.add_comment, name='comment'),  # get?? method preview
    path(r'post/<int:post_id>/edit', views.add_comment, name='comment'),  # patch - in that page
]