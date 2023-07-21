from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_date(self, obj):
        return naturaltime(obj.created_date)

    def get_updated_date(self, obj):
        return naturaltime(obj.updated_date)

    class Meta:
        model = Comment
        fields = [
            'owner', 'created_date', 'updated_date',
            'content', 'profile_image', 'is_owner',
            'profile_id', 'post', 'id'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    This serializer is used in the detail view.
    """
    post = serializers.ReadOnlyField(source='post.id')