from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from blog.api.serializers import PostSerializer
from blog.models import Post




class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewDestroy(generics.DestroyAPIView):
    """
    API endpoint that allows delete post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewList(generics.ListAPIView):
    """
    API endpoint that shows posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewsDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows retrieve post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer