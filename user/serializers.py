from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
