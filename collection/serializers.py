from rest_framework import serializers

from user.serializers import UserSerializer
from usergroup.serializers import UserGroupSerializer
from utils.serializers import UploadFileDetailSerializer
from . import models


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = '__all__'


class CollectionDetailSerializer(serializers.ModelSerializer):
    usergroup = UserGroupSerializer(many=True)
    template_file = UploadFileDetailSerializer()
    creator = UserSerializer

    class Meta:
        model = models.Collection
        fields = '__all__'
