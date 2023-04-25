from django.contrib.auth import get_user_model
from django.contrib.postgres.search import SearchVector
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import RedirectView, ListView
from django.utils.http import urlencode
from posts.models import Post


class IndexView(ListView):
    template_name = "index.html"
    model = Post
    context_object_name = "posts"
    ordering = ("-created_at",)

    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)
    #
    # def get_search_form(self):
    #     return SearchForm(self.request.GET)
    #
    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset, 1)
    #     if self.search_value:
    #         query = Q(author__username__icontains=self.search_value) | Q(description__icontains=self.search_value)
    #         print(query, 2)
    #         queryset = queryset.filter(query)
    #         print(queryset, 3)
    #     return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     # context['favorite_form'] = FavoriteForm()
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context




# def search_view(request: WSGIRequest):
#     form = SearchForm()
#     query = None
#     results = []
#     print(query)
#     if "query" in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             print(query,2)
#             query = form.cleaned_data["query"]
#
#             results = Account.objects.annotate(
#                 search=SearchVector("email"),
#             ).filter(search=query)
#             print(results)
#
#     context = {
#         "form": form,
#         "query": query,
#         "results": results,
#     }
#     return render(request, "index.html", context=context)


class IndexRedirectView(RedirectView):
    pattern_name = "index"

