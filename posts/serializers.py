from rest_framework import serializers
from .models import Post
from likes.models import Like
from favorite.models import Favorite


class UpdateMixin(serializers.ModelSerializer):
    def get_extra_kwargs(self):
        kwargs = super().get_extra_kwargs()
        no_update_fields = getattr(self.Meta, "no_update_fields", None)

        if self.instance and no_update_fields:
            for field in no_update_fields:
                kwargs.setdefault(field, {})
                kwargs[field]["read_only"] = True

        return kwargs


class PostSerializer(UpdateMixin, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    favorite_id = serializers.SerializerMethodField()
    favorite_count = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')

    def validate_post_image(self, value):
        """
        Throws error if the image width or height is larger than 4096px
        """
        if value.size > 1024 * 1024 * 4:
            raise serializers.ValidationError(
                'Image size larger than 4MB!')
        if value.image.width > 8192:
            raise serializers.ValidationError(
                'Image width larger than 8192px!')
        if value.image.height > 8192:
            raise serializers.ValidationError(
                'Image height larger than 8192px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_likes_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            likes = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return likes.id if likes else None
            print(likes)
        return None

    def get_favorite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favorite = Favorite.objects.filter(
                owner=user, post=obj
            ).first()
            return favorite.id if favorite else None
        return None

    class Meta:
        model = Post
        no_update_fields = ["post_image"]
        fields = [
            'owner', 'created_date', 'updated_date',
            'caption', 'post_image', 'profile_image',
            'is_owner', 'profile_id', 'id', 'comments_count',
            'likes_id', 'likes_count','favorite_id', 'favorite_count',
        ]
