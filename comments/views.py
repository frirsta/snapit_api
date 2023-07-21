from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    Displays a list of all the comments and their information.
    The filterset_fields can find comments made by a specific user
    The filterset_fields can also find what comments have been made
    on a specific post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [
        DjangoFilterBackend]
    filterset_fields = [
        'post',
        'owner__comment__owner__profile'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Display comment detail.
    The owner of the comment can edit and delete their comment here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()