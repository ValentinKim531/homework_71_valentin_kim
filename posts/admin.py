from django.contrib import admin

from posts.models import Post, Comment


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "description",
        "author",
    )
    list_filter = (
        "id",
        "author",
    )
    search_fields = ("author",)
    fields = ("image", "description", "author")
    readonly_fields = ("id",)


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "post",
        "text",
    )
    list_filter = ("id", "author")
    search_fields = ("author",)
    fields = (
        "author",
        "post",
        "text",
    )
    readonly_fields = ("id",)


admin.site.register(Comment, CommentAdmin)
