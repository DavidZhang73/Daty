from rest_framework import serializers

from user.serializers import UserProfileSerializer
from . import models


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    user = UserProfileSerializer(required=False)

    class Meta:
        model = models.User
        fields = '__all__'



class UserGroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = models.UserGroup
        fields = [
            'id',
            'name',
            'type',
            'creator',
            'users',
            'created_datetime',
            'last_modified_datetime'
        ]
        read_only_fields = [
            'creator'
        ]

    def save(self, **kwargs):
        print(self.validated_data)


class UserGroupListSerializer(serializers.ModelSerializer):
    users_count = serializers.IntegerField(source='get_users_count', read_only=True)

    class Meta:
        model = models.UserGroup
        fields = [
            'id',
            'name',
            'type',
            'users_count',
            'created_datetime',
            'last_modified_datetime'
        ]
