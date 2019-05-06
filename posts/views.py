from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DateDetailView, FormView, UpdateView, CreateView
from django.views import View
from django.utils import timezone

from .models import Post, Comment, Category


class PostList(ListView):
    published = True
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # TODO: how add the most popular posts by views?
        return context

    def get_queryset(self):
        return Post.objects.filter(published=self.published,
                                   date__lt=timezone.now()).order_by('-date')


class PostView(DetailView):
    model = Post
    context_object_name = 'post'


class PostPreviewView(DetailView):
    model = Post
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    fields = ['published', 'date', 'title', 'content']
    template_name = 'post_form.html'


class UpdatePostView(UpdateView):
    model = Post
    fields = ['published', 'date', 'title', 'content']
    template_name = 'post_form.html'


# TODO: change directory with templates to turn correct reusable static
