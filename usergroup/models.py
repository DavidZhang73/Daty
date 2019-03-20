from django.db import models

from user.models import User as _User

type_choice = [
    ('NONEEDLOGIN', '不需要登陆'),
    ('ALREADYSIGNIN', '需要登陆已注册'),
    ('REQUIRESIGNIN', '需要登陆未注册'),
]


class User(models.Model):
    name = models.CharField('名称', max_length=128, null=True, blank=True)
    user = models.ForeignKey(verbose_name='已经注册的用户', to=_User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField('邮箱', null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name} {self.user} {self.email}'


class UserGroup(models.Model):
    name = models.CharField('名称', max_length=128)
    type = models.CharField('类型', max_length=20, choices=type_choice)
    creator = models.ForeignKey(verbose_name='创建人', to=_User, on_delete=models.CASCADE)
    users = models.ManyToManyField(verbose_name='用户', to=User)
    created_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_datetime = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '用户组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_users_count(self):
        return self.users.count()
