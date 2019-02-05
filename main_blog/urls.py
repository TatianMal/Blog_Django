from django.urls import path
from . import views

app_name = 'main_blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail_post, name='detail'),
    path('<int:post_id>/comment', views.add_comment, name='comment'),
]