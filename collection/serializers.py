from rest_framework import serializers

from user.serializers import UserSerializer
from utils.serializers import UploadFileSerializer
from usergroup.serializers import UserSerializer as UserGroupUserSerializer
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


class CollectionFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CollectionFile
        fields = ['id', 'file']


class CollectionFileDetailSerializer(serializers.ModelSerializer):
    file = UploadFileSerializer()
    uploader = UserGroupUserSerializer()

    class Meta:
        model = models.CollectionFile
        fields = '__all__'
