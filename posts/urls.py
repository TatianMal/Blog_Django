from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='index'),  # get with filter
    path(r'unpublished/', views.PostList.as_view(published=False), name='unpublished_posts'),
    path(r'post/create/', views.CreatePostView.as_view(), name='create_post'),  # post - in that page
    path(r'post/<int:post_id>/', views.PostView.as_view(), name='view_post'),  # get
    path(r'post/<int:post_id>/preview/', views.PostPreviewView.as_view(), name='preview_post'),  # get?? method preview
    path(r'post/<int:post_id>/edit/', views.UpdatePostView.as_view(), name='update_post'),  # patch - in that page
]
