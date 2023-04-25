from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from django.utils.http import urlencode
from accounts.forms import LoginForm, CustomUserCreationForm, UserChangeForm, PasswordChangeForm, SearchForm
from accounts.models import Account
from posts.models import Post


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Некорректные данные")
            return redirect('index')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if not user:
            messages.warning(request, "Пользователь не найден")
            return redirect('index')
        login(request, user)
        messages.success(request, 'Добро пожаловать')
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        posts = self.object.posts.all()
        paginator = Paginator(posts, self.paginate_related_by,
                              orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['posts'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class ProfileReadOnlyView(DetailView):
    model = Account
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        posts = self.object.posts.all()
        paginator = Paginator(posts, self.paginate_related_by,
                              orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['posts'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('login')

    def test_func(self):
        return self.request.user == self.get_object()


class SearchView(ListView):
    template_name = "index_search.html"
    model = Account
    context_object_name = "accounts"

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            print(self.form.cleaned_data['query'], 0)
            return self.form.cleaned_data['query']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset, 1)
        if self.search_value:
            query = Q(email__icontains=self.search_value) | Q(first_name__icontains=self.search_value) | \
                    Q(last_name__icontains=self.search_value)
            print(query, 2)
            queryset = queryset.filter(query)
            print(queryset, 3)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        print(context, 8)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            print(context, 9)
        return context

@login_required
def unsubscribe_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    user_by_pk = get_object_or_404(Account, pk=pk)
    user_from_request.subscriptions.remove(user_by_pk)
    return redirect('profile', pk=pk)


@login_required
def subscribe_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    user_by_pk = get_object_or_404(Account, pk=pk)
    user_from_request.subscriptions.add(user_by_pk)
    return redirect('profile', pk=pk)


@login_required
def like_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    post_by_pk = get_object_or_404(Post, pk=pk)
    post_by_pk.user_likes.add(user_from_request)
    if 'post' in request.META.get('HTTP_REFERER'):
        return redirect('post_detail', pk=pk)
    return redirect('post_index_redirect')

@login_required
def unlike_view(request: WSGIRequest, pk):
    user_from_request: Account = request.user
    post_by_pk = get_object_or_404(Post, pk=pk)
    post_by_pk.user_likes.remove(user_from_request)
    if 'post' in request.META.get('HTTP_REFERER'):
        return redirect('post_detail', pk=pk)
    return redirect('post_index_redirect')


class SubscribersListView(TemplateView):
    template_name = 'account_subscribers.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        user = get_object_or_404(Account, pk=pk)
        print(user)
        context = {
            'user_obj': user
        }
        return context


class SubscriptionsListView(TemplateView):
    template_name = 'account_subscriptions.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        user = get_object_or_404(Account, pk=pk)
        print(user)
        context = {
            'user_obj': user
        }
        return context

