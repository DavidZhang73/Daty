from rest_framework import serializers

from user.serializers import UserSerializer
from utils.serializers import UploadFileSerializer
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
    template_file = UploadFileSerializer()

    class Meta:
        model = models.Collection
        fields = '__all__'
