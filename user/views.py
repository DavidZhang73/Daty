from django.contrib import auth

from .serializers import LoginSerializer
from utils.api import API
from utils.decorators import validate_serializer


class LoginAPI(API):
    @validate_serializer(LoginSerializer)
    def post(self, request):
        data = request.validated_data
        user = auth.authenticate(email=data["email"], password=data["password"])
        if user:
            if not user.is_active:
                return self.error("您的账户被关闭")
            else:
                auth.login(request, user)
                return self.success("success")
        else:
            return self.error('Email或密码不正确')


class LogoutAPI(API):
    def get(self, request):
        auth.logout(request)
        return self.success("success")
