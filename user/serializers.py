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
            'email',
            'username',
            'phone',
            'qq'
        ]
        extra_kwargs = {
            'email': {'required': False, 'read_only': True}
        }


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(label='新密码')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(label='密码')


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SiginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SigninUserInfo
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'date_joined': {"read_only": True}
        }


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForgetPassword
        fields = '__all__'
        read_only_fields = [
            'id',
            'created_datetime'
        ]


class ForgetPasswordResetSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    password = serializers.CharField(label='密码')
