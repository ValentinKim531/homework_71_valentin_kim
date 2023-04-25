from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'avatar', 'birth_date')
    list_filter = ('id', 'email', 'birth_date')
    search_fields = ('email', 'birth_date')
    fields = ('email', 'avatar', 'birth_date', 'liked_posts', 'subscriptions', 'commented_posts')
    readonly_fields = ('id',)


admin.site.register(Account, AccountAdmin)
