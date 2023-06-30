from .models import Follower
from .serializers import FollowerSerializer
from rest_framework import generics, permissions
from api.permissions import IsOwnerOrReadOnly

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetails(generics.RetrieveUpdateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
