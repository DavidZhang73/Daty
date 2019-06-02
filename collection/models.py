import uuid

from django.db import models

from user.models import User
from usergroup.models import UserGroup
from utils.models import UploadFile


class Collection(models.Model):
    id = models.UUIDField('ID', default=uuid.uuid1, primary_key=True)
    name = models.CharField('名称', max_length=128)
    description = models.CharField('要求', max_length=300, blank=True, null=True)
    usergroup = models.ManyToManyField(verbose_name='用户组', to=UserGroup)
    start_datetime = models.DateTimeField('开始日期时间')
    end_datetime = models.DateTimeField('结束日期时间')
    template_file = models.ForeignKey(verbose_name='模板文件', to=UploadFile, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField('创建日期时间', auto_now_add=True)
    creator = models.ForeignKey(verbose_name='创建人', to=User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文件集'
        verbose_name_plural = verbose_name
