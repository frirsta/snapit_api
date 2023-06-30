from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Video
        fields = ['owner', 'is_owner', 'id', 'created_date',
                  'updated_date', 'caption', 'profile_image',
                  'profile_id', 'owner_id', 'video', 'file']
