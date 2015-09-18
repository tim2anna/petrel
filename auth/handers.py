#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyrestful import mediatypes
from pyrestful.rest import get
from tornado.web import asynchronous, gen, addslash

from libs.base_handler import BaseHandler
from auth.models import User


class UserHandler(BaseHandler):

    @get(_path="/users/")
    @asynchronous
    @gen.coroutine
    def users(self):
        resp = yield User.objects.limit(10).order_by("username").find_all()
        self.render_json({'123': len(resp)})

    def users_callback(self, user_set):
        self.write('123')
        return 456

    @asynchronous
    @get(_path="/users/create", _produces=mediatypes.APPLICATION_JSON)
    def users_create(self):
        user = User(username="Bernardo", password="Heynemann")
        user.save(self.users_create_callback)
        return {123:456}

    def users_create_callback(self, user):
        self.write('123')
        self.finish()
        return 456

    # def users_create(self):
