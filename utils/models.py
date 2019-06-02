import uuid

from django.conf import settings
from django.db import models

from user.models import User


class UploadFile(models.Model):
    id = models.UUIDField('ID', default=uuid.uuid1, primary_key=True)
    name = models.CharField('文件名', max_length=256)
    file = models.FileField('文件', upload_to='file', max_length=1024)
    uploader = models.ForeignKey(verbose_name='上传用户', to=User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField('上传日期', auto_now_add=True)

    class Meta:
        verbose_name = '上传文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        super(UploadFile, self).delete()

    def get_url(self):
        return f'{settings.MEDIA_URL}{self.file}'
