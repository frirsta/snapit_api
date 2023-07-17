from rest_framework import serializers
from .models import Post


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
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        no_update_fields = ["post_image"]
        fields = [
            'owner', 'created_date', 'updated_date',
            'caption', 'post_image', 'profile_image',
            'is_owner', 'profile_id', 'id',
        ]
