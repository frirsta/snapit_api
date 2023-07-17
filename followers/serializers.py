from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    now_follower = serializers.ReadOnlyField(source='follower.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'created_date', 'follower', 'owner', 'now_follower'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible dublicate'
            })