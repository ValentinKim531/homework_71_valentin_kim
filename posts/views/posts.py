from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from posts.forms import PostForm
from posts.models import Post


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "post_create.html"
    model = Post
    form_class = PostForm
    success_message = "Пост добавлен"
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class PostDetail(DetailView):
    template_name = "post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        context["comments"] = comments
        return context

