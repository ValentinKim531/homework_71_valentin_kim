from django.urls import path

from posts.views.base import IndexRedirectView, IndexView
from posts.views.comments import CommentDetailView, PostCommentCreateView
from posts.views.posts import PostDetail, PostCreateView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "post/", IndexRedirectView.as_view(), name="post_index_redirect"
    ),
    path("post/add", PostCreateView.as_view(), name="post_add"),
    path("post/<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("review/<int:pk>", CommentDetailView.as_view(), name="comment_detail"),
    path('post/<int:pk>/comments/add/', PostCommentCreateView.as_view(), name='post_comment_add'),
]
