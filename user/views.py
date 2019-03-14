from django.conf import settings
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from django.shortcuts import HttpResponseRedirect

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from utils.api import API, APIViewSet
from utils.decorators import validate_serializer


class UserViewSet(APIViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(methods=['post'], detail=False, description='用户登录')
    @validate_serializer(serializers.LoginSerializer)
    def login(self, request):
        data = request.validated_data
        user = auth.authenticate(email=data.get('email'), password=data.get("password"))
        if user:
            if not user.is_active:
                return self.error("您的账户未激活或被关闭，请检查邮箱或者联系管理员")
            else:
                auth.login(request, user)
                return self.success({
                    'id': user.id,
                    'username': user.username,
                })
        else:
            return self.error('Email不存在或密码不正确')

    @action(methods=['get'], detail=False, description='用户登出')
    def logout(self, request):
        auth.logout(request)
        return self.success("success")

    @action(methods=['post'], detail=False, description='验证邮箱是否存在'
            )
    @validate_serializer(serializers.CheckEmailSerializer)
    def checkEmail(self, request):
        data = request.validated_data
        email = data.get('email')
        if models.User.objects.filter(email=email):
            return self.success('Email已注册')
        else:
            return self.success('Email未注册')

    @action(methods=['post'], detail=False, description='用户注册')
    @validate_serializer(serializers.SiginSerializer)
    def signin(self, request):
        data = request.validated_data
        email = data.get('email')
        username = data.get('username')
        phone = data.get('phone')
        qq = data.get('qq')
        password = data.get('password')
        if models.User.objects.filter(email=email):
            return self.error('Email已注册')
        else:
            user = models.SigninUserInfo.objects.create(
                username=username,
                password=make_password(password),
                email=email,
                phone=phone,
                qq=qq,
            )
            url = '/api/user/signinActive/' + str(user.id)
            send_mail(
                subject=f'{settings.EMAIL_SUBJECT_PREFIX} 注册新账号',
                message=f'请点击此链接完成注册：\n{settings.HOST}{url}\n如果不是您本人的操作，请忽略这条邮件。',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )
            return self.success(f'成功注册用户：{email}')

    @action(methods=['post'], detail=False, description='用户忘记密码')
    @validate_serializer(serializers.ForgetPasswordSerializer)
    def forgetPassword(self, request):
        data = request.validated_data
        email = data.get('email')
        user = models.User.objects.filter(email=email)
        if not user:
            return self.error('Email未注册')
        else:
            forgetPassword = models.ForgetPassword.objects.create(
                email=email
            )
            url = '/api/user/forgetPasswordReset/' + str(forgetPassword.id)
            user[0].email_user(
                subject=f'{settings.EMAIL_SUBJECT_PREFIX} 重置密码',
                message=f'请点击此链接重置密码：\n{settings.HOST}{url}\n如果不是您本人的操作，请忽略这条邮件。'
            )
            return self.success(f'请在{email}中继续找回密码的操作')

    @action(methods=['post'], detail=False, description='用户忘记密码重置')
    @validate_serializer(serializers.ForgetPasswordResetSerializer)
    def forgetPasswordReset(self, request):
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


class ProfileAPI(API):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        s = serializers.UserProfileSerializer(user)
        return self.success(s.data)

    @validate_serializer(serializers.UserProfileSerializer)
    def patch(self, request):
        data = request.validated_data
        user = request.user
        user.username = data.get('username')
        user.phone = data.get('phone')
        user.qq = data.get('qq')
        user.save()
        s = serializers.UserProfileSerializer(user)
        return self.success(s.data)


class ChangePasswordAPI(API):
    permission_classes = (IsAuthenticated,)

    @validate_serializer(serializers.ChangePasswordSerializer)
    def post(self, request):
        user = request.user
        data = request.validated_data
        new_password = data.get('new_password')
        user.set_password(new_password)
        user.save()
        return self.success("success")
