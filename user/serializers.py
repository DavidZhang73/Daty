from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'username',
            'phone',
            'qq'
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SiginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SigninUserInfo
        fields = '__all__'


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForgetPassword
        fields = '__all__'


class ForgetPasswordResetSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    password = serializers.CharField()
