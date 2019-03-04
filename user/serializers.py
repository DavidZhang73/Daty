from rest_framework import serializers
from . import models


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class SigninEmailCheckSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SiginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SigninUserInfo
        fields = '__all__'


class ForgetPasswordEmailCheckSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForgetPassword
        fields = '__all__'


class ForgetPasswordResetSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    password = serializers.CharField()
