from rest_framework import serializers

from user.serializers import UserSerializer
from . import models


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = '__all__'
        kwargs = {
            'creator': {'read_only': True}
        }


class CollectionDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = models.Collection
        fields = '__all__'
