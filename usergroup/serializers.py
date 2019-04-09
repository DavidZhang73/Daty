from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserGroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    users_count = serializers.IntegerField(source='get_users_count', read_only=True)

    class Meta:
        model = models.UserGroup
        fields = [
            'id',
            'name',
            'type',
            'creator',
            'users_count',
            'users',
            'created_datetime',
            'last_modified_datetime'
        ]
        read_only_fields = [
            'creator',
            'created_datetime',
            'last_modified_datetime'
        ]

    def save(self, **kwargs):
        print(self.validated_data)
