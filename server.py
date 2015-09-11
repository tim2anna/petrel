#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import pyrestful.rest

from settings import INSTALLED_APPS
from libs.handler_finder import HandlerFinder


ROOT_PATH = os.path.dirname(__file__)


if __name__ == '__main__':
    finder = HandlerFinder(root_path=ROOT_PATH)
    finder.find(INSTALLED_APPS)

    app = pyrestful.rest.RestService(finder.handlers)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
