from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View

from .models import Post, Comment, Category


class PostList(ListView):
    arg = 'hii'
    model = Post
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        if(kwargs.get('arg') is not None):
            context['arg'] = kwargs['arg']
        else:
            context['arg'] = 'Test arg'
        # TODO: how add the most popular posts by views?
        return context


class PostView(View):
    pass


# TODO: change directory with templates to turn correct reusable static
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
    try:
        selected_comment = post.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'main_blog/detail.html', {
            'post': post,
            'error_message': 'You didn\'t select a comment'
        })
    else:
        selected_comment

    return render(request, 'comments.html', {'post': post})