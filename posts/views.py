from rest_framework import generics, permissions, filters
from posts.models import Post
from .serializers import PostSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        'owner__profile',
    ]
    ordering_fields = [
        'comments_count',
    ]
    search_fields = [
        'owner__username',
        'caption'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_date')

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = [
        'comments_count',
    ]
    search_fields = [
        'owner__username',
        'caption'
    ]
