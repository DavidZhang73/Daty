from rest_framework import serializers

from user.serializers import UserSerializer
from . import models


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'


class UploadFileDetailSerializer(serializers.ModelSerializer):
    uploader = UserSerializer()

    class Meta:
        model = models.UploadFile
        fields = '__all__'
