from rest_framework.viewsets import ModelViewSet
from api.permissions import PostPermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import PostSerializer
from posts.models import Post



class PostView(ModelViewSet):
    permission_classes = [PostPermission, IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

