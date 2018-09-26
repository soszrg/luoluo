# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from upload.views import *

urlpatterns = [
    url(r'picture/$', PictureView.as_view())
]