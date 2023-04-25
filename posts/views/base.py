from django.views.generic import RedirectView, ListView
from posts.models import Post


class IndexView(ListView):
    template_name = "index.html"
    model = Post
    context_object_name = "posts"
    ordering = ("-created_at",)



class IndexRedirectView(RedirectView):
    pattern_name = "index"

