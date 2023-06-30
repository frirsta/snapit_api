from profiles.models import Profile
from .serializers import UserSerializer
from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
