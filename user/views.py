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
            send_mail(
                subject=f'{settings.EMAIL_SUBJECT_PREFIX} 注册新账号',
                message=f'请点击此链接完成注册：\n{settings.HOST}{url}\n如果不是您本人的操作，请忽略这条邮件。',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )
            return self.success(f'成功注册用户：{email}')


class SigninUserActive(View):
    def get(self, request, uuid):
        signinUserInfo = models.SigninUserInfo.objects.filter(id=uuid)
        if signinUserInfo:
            signinUserInfo[0].saveToUser()
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
        user = models.User.objects.filter(email=email)
        if not user:
            return self.error('Email不存在')
        else:
            forgetPassword = models.ForgetPassword.objects.create(
                email=email
            )
            url = '/api/user/forgetPassword/reset/' + str(forgetPassword.id)
            user[0].email_user(
                subject=f'{settings.EMAIL_SUBJECT_PREFIX} 重置密码',
                message=f'请点击此链接重置密码：\n{settings.HOST}{url}\n如果不是您本人的操作，请忽略这条邮件。'
            )
            return self.success(f'请在{email}中继续找回密码的操作')


class ForgetPasswordReset(View):
    def get(self, request, uuid):
        forgetPassword = models.ForgetPassword.objects.filter(id=uuid)
        if forgetPassword:
            return HttpResponseRedirect('/#/forgetPassword/reset/' + str(uuid))
        else:
            return HttpResponseRedirect('/#/login')


class ForgetPasswordResetAPI(API):
    @validate_serializer(serializers.ForgetPasswordResetSerializer)
    def post(self, request):
        data = request.validated_data
        uuid = data.get('uuid')
        password = data.get('password')
        forgetPassword = models.ForgetPassword.objects.filter(id=uuid)
        if forgetPassword:
            email = forgetPassword[0].email
            forgetPassword[0].delete()
            user = models.User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return self.success(f'成功重置用户{email}的密码')
        else:
            return self.error(f'链接已失效')
