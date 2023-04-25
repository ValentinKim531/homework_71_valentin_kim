from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, UserPasswordChangeView, \
    SearchView, ProfileReadOnlyView, SubscribersListView, SubscriptionsListView, unsubscribe_view, subscribe_view, \
    like_view, unlike_view

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/<int:pk>', ProfileView.as_view(), name='profile'),
    path('account/<int:pk>', ProfileReadOnlyView.as_view(), name='profile_read_only'),
    path('account/<int:pk>/change', UserChangeView.as_view(), name='change'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('search/', SearchView.as_view(), name='search'),
    path('<int:pk>/subscribers/', SubscribersListView.as_view(), name='subscribers'),
    path('<int:pk>/subscriptions/', SubscriptionsListView.as_view(), name='subscriptions'),
    path('<int:pk>/unsubscribe', unsubscribe_view, name='unsubscribe'),
    path('<int:pk>/subscribe', subscribe_view, name='subscribe'),
    path('account/<int:pk>/like', like_view, name='like'),
    path('account/<int:pk>/unlike', unlike_view, name='unlike'),
]