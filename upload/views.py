# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from upload.models import Picture, PicturesInGallery, Gallery, PictureTags
from utils.common import get_logger

log = get_logger(__name__)


class PictureView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        pgs = Picture.objects.only("url", "headline")
        for one in pgs:
            print one.url
        with transaction.atomic():
            p = Picture.objects.select_for_update().get(pk=3)
            p.headline = 'p3'
            p.save(update_fields=['headline'])
        return Response('get ok!')
