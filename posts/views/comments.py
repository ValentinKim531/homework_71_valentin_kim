from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, CreateView

from posts.forms import PostCommentForm
from posts.models import Comment, Post


class CommentDetailView(DetailView):
    template_name = "comment.html"
    model = Comment


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = PostCommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return redirect('comment_detail', pk=post.pk)