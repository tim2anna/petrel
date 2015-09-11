#!/usr/bin/env python
#-*- coding:utf-8 -*-


DATABASES = {
    'web': {
        'url': 'mysql://root:123456@localhost/iqms_web',
        'encoding': 'utf-8',
        'echo': True,
    },
    'pbnet': {
        'url': 'mysql://root:123456@localhost/iqms_pbnet',
        'encoding': 'utf-8',
        'echo': True,
    },
    'mem': {
        'url': 'mysql://root:123456@localhost/iqms_mem',
        'encoding': 'utf-8',
        'echo': True,
    },
}

INSTALLED_APPS = [
    'auth',
]

try:
    from local_settings import *
except Exception:
    pass
