# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.
from utils.common import timestamp_now


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    gender = models.CharField(default='', max_length=5, verbose_name="性别")


class ModelPermissions(models.Model):
    class Meta:
        permissions = (
            ('profile.admin', "添加企业管理员"),
            ('profile.create', "添加用户"),
            ('profile.update', "更新用户"),
            ('profile.delete', "删除用户"),
        )


class AbstractUser(AbstractBaseUser):
    phone = models.CharField(max_length=20, db_index=True, default='', blank=True)
    email = models.EmailField(db_index=True, default='', blank=True)
    joined_time = models.IntegerField(default=timestamp_now)
    last_login_ts = models.IntegerField(default=timestamp_now, blank=True, null=True)

    USERNAME_FIELD = 'phone'

    class Meta:
        abstract = True

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass


class AppUser(AbstractUser):
    client_type = models.CharField(max_length=10, default='', blank=True)

    class Meta(AbstractUser.Meta):
        ordering = ['-last_login_ts']
