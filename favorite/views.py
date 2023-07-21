from rest_framework import permissions, generics
from api.permissions import IsOwnerOrReadOnly
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteList(generics.ListCreateAPIView):
    """
    Displays a list of all the Favorites and their information.
    The filterset_fields can find Saved Posts made by a specific user
    The filterset_fields can also find what Saved Posts have been made
    on a specific post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    Display Favorite detail.
    The owner of the Saved Post can delete their Saved Post here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer