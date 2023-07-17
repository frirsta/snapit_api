from profiles.models import Profile
from .serializers import UserSerializer
from rest_framework import generics, filters
from api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

# Create your views here.


class UserList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        follower_count=Count(
            'owner__follower', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_date')
    serializer_class = UserSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'posts_count',
        'follower_count',
        'following_count',
    ]
    filterset_fields = [
        'owner__following__follower__profile',
        'owner__follower__owner__profile',
    ]
    search_fields = ['owner__username']


class UserDetails(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        follower_count=Count(
            'owner__follower', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_date')
    serializer_class = UserSerializer
