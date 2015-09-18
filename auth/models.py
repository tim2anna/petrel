#!/usr/bin/python
# -*- coding: utf-8 -*-


from motorengine import Document, StringField


class User(Document):
    """ 用户 """
    username = StringField(required=True)
    password = StringField(required=True)