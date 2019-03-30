from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from posts.models import Comment


class CommentsView(ListView):
    model = Comment
    context_object_name = 'all_comment'
    template_name = 'accounts/comments.html'
    # TODO: done that with session keys for safety other users


class AccountView(DetailView):
    model = get_user_model()
    template_name = 'accounts/account.html'
    context_object_name = 'user_obj'
    # TODO: done that with session keys for safety other users
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_comments'] = Comment.objects.filter(id__lte=2)
        return context