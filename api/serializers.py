from rest_framework import serializers

from accounts.models import Account
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

