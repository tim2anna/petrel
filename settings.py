#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os


INSTALLED_APPS = [
    'auth',
]


app_settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "debug": True,
    "session": {
        'engine': 'memcached',
        'storage': {'servers': ('localhost:11211',)},
        'cookies': {'expires_days': 120},
    }
}

SERVER_PORT = 8888

MONGODB_CONNECT = {
    'database': 'petrel',
    'host': 'localhost',
    'port': 27017
}

try:
    from local_settings import *
except Exception:
    pass
