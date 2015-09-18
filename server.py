#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import pyrestful.rest
import settings
from motorengine.connection import connect
from libs.handler_finder import HandlerFinder


ROOT_PATH = os.path.dirname(__file__)


if __name__ == '__main__':
    finder = HandlerFinder(root_path=ROOT_PATH)
    finder.find(settings.INSTALLED_APPS)

    app = pyrestful.rest.RestService(finder.handlers, **settings.app_settings)
    app.listen(settings.SERVER_PORT)

    io_loop = tornado.ioloop.IOLoop.instance()
    connect(
        settings.MONGODB_CONNECT['database'],
        host=settings.MONGODB_CONNECT['host'],
        port=settings.MONGODB_CONNECT['port'],
        io_loop=io_loop
    )
    print 'Web Server starting......'
    io_loop.start()