# Generated by Django 2.1.7 on 2019-03-20 17:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('usergroup', '0003_usergroup_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, verbose_name='已经注册的用户'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='type',
            field=models.CharField(
                choices=[('NO NEED LOGIN', '不需要登陆'), ('ALREADY SIGNIN', '需要登陆已注册'), ('REQUIRE SIGNIN', '需要登陆未注册')],
                max_length=10, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(to='usergroup.User', verbose_name='用户'),
        ),
    ]