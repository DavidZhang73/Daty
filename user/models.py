import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        '姓名',
        max_length=150,
        unique=False,
        help_text='必填。150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。',
        validators=[username_validator]
    )
    email = models.EmailField('Email', unique=True, error_messages={
        'unique': 'Email已经被注册',
    })
    phone = models.CharField('手机号', max_length=11, blank=True)
    qq = models.CharField('QQ', max_length=20, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta(AbstractUser.Meta):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class SigninUserInfo(models.Model):
    username_validator = UnicodeUsernameValidator()
    id = models.CharField('ID', max_length=36, default=uuid.uuid1, primary_key=True)
    email = models.EmailField('Email')
    username = models.CharField(
        '姓名',
        max_length=150,
        help_text='必填。150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。',
        validators=[username_validator]
    )
    phone = models.CharField('手机号', max_length=11, blank=True)
    qq = models.CharField('QQ', max_length=20, blank=True)
    password = models.CharField('密码', max_length=128)
    date_joined = models.DateTimeField('注册日期', default=timezone.now)

    class Meta:
        verbose_name = '注册信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def saveToUser(self):
        '''
        邮箱激活后，把SigninUserInfo中的信息放到User中，删除本身
        :return:
        '''
        User.objects.create(
            username=self.username,
            password=self.password,
            email=self.email,
            phone=self.phone,
            qq=self.qq,
            date_joined=self.date_joined
        ).save()
        self.delete()


class ForgetPassword(models.Model):
    id = models.CharField('ID', max_length=36, default=uuid.uuid1, primary_key=True)
    email = models.EmailField('Email')
    created_datetime = models.DateTimeField('时间', default=timezone.now)

    class Meta:
        verbose_name = '忘记密码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
