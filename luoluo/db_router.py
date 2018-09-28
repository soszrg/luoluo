# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings

DATABASE_APPS_MAPPING = settings.DATABASE_APPS_MAPPING


class CommonRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        obj1_db = DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        obj2_db = DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if obj1_db and obj2_db:
            if obj1_db == obj2_db:
                return True
            else:
                return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in DATABASE_APPS_MAPPING.values():
            return DATABASE_APPS_MAPPING.get(app_label) == db
        elif app_label in DATABASE_APPS_MAPPING:
            return False
        return None

