#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import pyrestful.rest
import xml.dom.minidom

from tornado.web import HTTPError
from pyrestful import mediatypes
from pyconvert.pyconv import convert2JSON, convert2XML


class BaseHandler(pyrestful.rest.RestHandler):

    def render_json(self, resp):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header("Content-Type", mediatypes.APPLICATION_JSON)
        if hasattr(resp, '__module__'):
            resp = convert2JSON(resp)
        if isinstance(resp, dict):
            self.write(resp)
        elif isinstance(resp, list):
            self.write(json.dumps(resp))
        self.finish()

    def render_xml(self, resp):
        self.set_header("Content-Type", mediatypes.APPLICATION_XML)
        if hasattr(resp, '__module__'):
            resp = convert2XML(resp)
        if isinstance(resp, xml.dom.minidom.Document):
            self.write(resp.toxml())
        self.finish()