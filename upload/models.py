# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from profiles.models import Profile
from utils.common import timestamp_now


class Picture(models.Model):
    headline = models.CharField(max_length=200, verbose_name='标题')
    url = models.URLField(max_length=200, verbose_name="下载链接")
    owner_id = models.SmallIntegerField(default=-1, verbose_name="上传者")
    description = models.TextField(default='')
    upload_time = models.IntegerField(default=timestamp_now)
    update_time = models.IntegerField(default=timestamp_now)

    def __str__(self):
        return self.headline


class Gallery(models.Model):
    headline = models.CharField(max_length=200, verbose_name='标题')
    description = models.TextField(default='')
    upload_time = models.IntegerField(default=timestamp_now)
    update_time = models.IntegerField(default=timestamp_now)

    def __str__(self):
        return self.headline


class PicturesInGallery(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True,
                                related_name="p_i_gs",)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    joined_time = models.IntegerField(default=timestamp_now)

    class Meta:
        db_table = "upload_pictures_in_gallery"
        ordering = ('joined_time',)

    def __str__(self):
        return "{0.gallery.headline}->{0.picture.headline}".format(self)


class Tag(models.Model):
    content = models.CharField(max_length=200, default="")
    p_tag = models.ForeignKey('self', null=True, blank=True)
    commit_time = models.IntegerField(default=timestamp_now)
    update_time = models.IntegerField(default=timestamp_now)

    class Meta:
        ordering = ("-update_time",)

    def __str__(self):
        return "{}".format(self.id)


class PictureTags(models.Model):
    picture = models.ForeignKey(Picture, related_name="pts_pic", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="pts_tag")


class PkStudy(models.Model):
    title = models.CharField(max_length=20, primary_key=True)
    content = models.CharField(max_length=50)
