# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

import time


def get_logger(name):
    return logging.getLogger('django.' + name)


def timestamp_now():
    return int(time.time())
