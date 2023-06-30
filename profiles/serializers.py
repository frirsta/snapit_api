from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follower_id = serializers.SerializerMethodField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_follower_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            follower = Follower.objects.filter(
                owner=user, following=obj.owner
            ).first()
            return follower.id if follower else None
        return None

    class Meta:
        model = Profile
        fields = ['owner', 'is_owner', 'id', 'created_date',
                  'updated_date', 'bio', 'profile_image', 'follower_id',
                  'follower_count', 'following_count', 'posts_count']
