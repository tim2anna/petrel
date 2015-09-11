#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get


class UserHandler(pyrestful.rest.RestHandler):

    @get(_path="/echo/{name}", _produces=mediatypes.APPLICATION_JSON)
    def sayHello(self, name):
        return {"Hello": name}
