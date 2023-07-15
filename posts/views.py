from rest_framework import generics, permissions, filters
from posts.models import Post
from .serializers import PostSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'caption'
    ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetails(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter]
    search_fields = [
        'owner__username',
        'caption'
    ]
