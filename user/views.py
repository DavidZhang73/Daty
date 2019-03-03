from django.conf import settings
from django.core.mail import send_mail

from django.contrib import auth
from django.views.generic.base import View
from django.shortcuts import HttpResponseRedirect

from . import serializers
from . import models
from utils.api import API
from utils.decorators import validate_serializer


class LoginAPI(API):
    @validate_serializer(serializers.LoginSerializer)
    def post(self, request):
        data = request.validated_data
        user = auth.authenticate(email=data.get('email'), password=data.get("password"))
        if user:
            if not user.is_active:
                return self.error("您的账户未激活或被关闭，请检查邮箱或者联系管理员")
            else:
                auth.login(request, user)
                return self.success({
                    'email': user.email,
                    'username': user.username,
                    'qq': user.qq,
                    'phone': user.phone
                })
        else:
            return self.error('Email不存在或密码不正确')


class LogoutAPI(API):
    def get(self, request):
        auth.logout(request)
        return self.success("success")


class SigninEmailCheckAPI(API):
    @validate_serializer(serializers.SigninEmailCheckSerializer)
    def post(self, request):
        data = request.validated_data
        email = data.get('email')
        if models.User.objects.filter(email=email):
            return self.success('Email已经被注册')
        else:
            return self.success('Email可以注册')


class SigninAPI(API):
    @validate_serializer(serializers.SiginSerializer)
    def post(self, request):
        data = request.validated_data
        email = data.get('email')
        username = data.get('username')
        phone = data.get('phone')
        qq = data.get('qq')
        password = data.get('password')
        if models.User.objects.filter(email=email):
            return self.error('Email已经被注册')
        else:
            user = models.SigninUserInfo.objects.create(
                username=username,
                password=password,
                email=email,
                phone=phone,
                qq=qq,
            )
            url = '/api/user/signin/active/' + str(user.id)
            print(url)
            # TODO 发送url到邮箱
            return self.success(f'成功注册用户：{email}')


class SigninUserActive(View):
    def get(self, request, uuid):
        models.SigninUserInfo.objects.get(id=uuid).saveToUser()
        return HttpResponseRedirect('/#/login')


class ForgetPasswordEmailCheckAPI(API):
    @validate_serializer(serializers.ForgetPasswordEmailCheckSerializer)
    def post(self, request):
        data = request.validated_data
        email = data.get('email')
        if models.User.objects.filter(email=email):
            return self.success('Email存在')
        else:
            return self.success('Email不存在')


class ForgetPasswordAPI(API):
    @validate_serializer(serializers.ForgetPasswordSerializer)
    def post(self, request):
        data = request.validated_data
        email = data.get('email')
        if not models.User.objects.filter(email=email):
            return self.error('Email不存在')
        else:
            forgetPassword = models.ForgetPassword.objects.create(
                email=email
            )
            url = '/api/user/forgetPassword/reset/' + str(forgetPassword.id)
            print(url)
            # TODO 发送url到邮箱
            return self.success(f'请在{email}中继续找回密码的操作')


class ForgetPasswordReset(View):
    def get(self, request, uuid):
        models.ForgetPassword.objects.get(id=uuid)
        return HttpResponseRedirect('/#/forgetPassword/reset/' + str(uuid))


class ForgetPasswordResetAPI(API):
    @validate_serializer(serializers.ForgetPasswordResetSerializer)
    def post(self, request):
        data = request.validated_data
        uuid = data.get('uuid')
        password = data.get('password')
        email = models.ForgetPassword.objects.get(id=uuid).email
        user = models.User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return self.success(f'成功重置用户{email}的密码')
