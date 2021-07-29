from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from blog.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    def get_queryset(self):
        return Post.postobjects.all()