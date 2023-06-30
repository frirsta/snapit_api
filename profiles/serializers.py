from rest_framework import serializers
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = ['owner', 'is_owner', 'id', 'created_date',
                  'updated_date', 'bio', 'profile_image']
