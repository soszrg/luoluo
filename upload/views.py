# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile
from utils.common import get_logger

log = get_logger(__name__)


class PictureView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        log.error('<======log output test======>')
        ps = User.objects.all()
        for p in ps:
            print p.username
        return Response('get ok!')
