from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.db.models import QuerySet
from django.shortcuts import HttpResponseRedirect
from django.template import loader
from django.views.generic.base import View
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from utils.email import send_email
from . import models
from . import serializers


class LoginAPIView(GenericAPIView):
    queryset = QuerySet()
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = auth.authenticate(email=data.get('email'), password=data.get("password"))
        if user:
            if not user.is_active:
                raise APIException("您的账户未激活或被关闭，请检查邮箱或者联系管理员")
            else:
                auth.login(request, user)
                return Response({
                    'id': user.id,
                    'username': user.username,
                })
        else:
            raise APIException('Email不存在或密码不正确')


class LogoutAPIView(GenericAPIView):
    queryset = QuerySet()
    serializer_class = Serializer()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        auth.logout(request)
        return Response("success")


class CheckEmailAPIView(GenericAPIView):
    queryset = QuerySet()
    serializer_class = serializers.CheckEmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data.get('email')
        if models.User.objects.filter(email=email):
            return Response('Email已注册')
        else:
            return Response('Email未注册')


class SigninAPIView(CreateAPIView):
    queryset = QuerySet()
    serializer_class = serializers.SiginSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        if models.User.objects.filter(email=email):
            raise APIException('Email已注册')
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        signin_user_info = serializer.save()
        url = '/api/user/signinActive/' + str(signin_user_info.id)
        send_email(
            subject=f'{settings.EMAIL_SUBJECT_PREFIX} 注册新账号',
            message=f'请点击此链接完成注册：\n{settings.HOST}{url}\n如果不是您本人的操作，请忽略这条邮件。',
            email=email
        )


class ForgetPasswordAPIView(CreateAPIView):
    queryset = QuerySet()
    serializer_class = serializers.ForgetPasswordSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        email = data.get('email')
        user = models.User.objects.filter(email=email)
        if not user:
            raise APIException('Email未注册')
        forgetPassword = serializer.save()
        url = '/api/user/forgetPasswordReset/' + str(forgetPassword.id)
        send_email(
            subject=f'{settings.EMAIL_SUBJECT_PREFIX} 重置密码',
            message=f'请点击此链接重置密码：\n{settings.HOST}{url}\n如果不是您本人的操作，请忽略这条邮件。',
            email=user[0].email,
            html_message=loader.render_to_string('', {})
        )


class ForgetPasswordResetAPIView(GenericAPIView):
    queryset = models.ForgetPassword.objects.all()
    serializer_class = serializers.ForgetPasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        uuid = data.get('uuid')
        password = data.get('password')
        forgetPassword = models.ForgetPassword.objects.filter(id=uuid)
        if forgetPassword:
            email = forgetPassword[0].email
            forgetPassword[0].delete()
            user = models.User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return Response(f'成功重置用户{email}的密码')
        else:
            raise APIException(f'链接已失效')


class ProfileAPIView(GenericAPIView):
    queryset = QuerySet()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(request.user, serializer.validated_data)
        return Response(serializer.validated_data)


class ChangePasswordAPIView(GenericAPIView):
    queryset = QuerySet()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        new_password = data.get('new_password')
        user.set_password(new_password)
        user.save()
        return Response("success")


class SigninActiveUser(View):
    def get(self, request, uuid):
        signinUserInfo = models.SigninUserInfo.objects.filter(id=uuid)
        if signinUserInfo:
            signinUserInfo[0].saveToUser()
            return HttpResponseRedirect('/#/user/signinSuccess')
        else:
            return HttpResponseRedirect('/#/user/login')


class ForgetPasswordReset(View):
    def get(self, request, uuid):
        forgetPassword = models.ForgetPassword.objects.filter(id=uuid)
        if forgetPassword:
            return HttpResponseRedirect('/#/user/forgetPassword/reset/' + str(uuid))
        else:
            return HttpResponseRedirect('/#/user/login')
