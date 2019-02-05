from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('id')[:5]  # acs, decs (-id)
    # output = ', '.join([post.title for post in latest_posts])
    # return HttpResponse('Hello, world!\n'+output)
    context = {'latest_posts': latest_posts}
    return render(request, 'index.html', context )


def detail_post(request, post_id):
    # try:
    #     post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     raise Http404('Post does not exist')
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'details.html', {'post': post})


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'comments.html', {'post': post})