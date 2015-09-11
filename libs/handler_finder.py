#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pyrestful.rest


class HandlerFinder(object):
    """ Handler发现器 """

    def __init__(self, root_path):
        self.root_path = root_path
        self.handlers = []

    def find(self, app_list):
        for app in app_list:
            self.get_handler(os.path.join(self.root_path, app))

    def get_handler(self, root_path):
        """ 在指定目录中获取handler类导入 """
        if not HandlerFinder.is_python_module(root_path):
            return

        for filename in os.listdir(root_path):
            path = os.path.join(root_path, filename)
            if os.path.isdir(path):
                self.get_handler(path)
            if self.is_python_file(path):
                relpath = os.path.relpath(path, self.root_path)
                dir_list = relpath[:-3].split('/')

                if dir_list[-1] == '__init__':
                    module = __import__('.'.join(dir_list[:-1]))
                else:
                    module = __import__('.'.join(dir_list), fromlist=dir_list[:-1])

                for item in module.__dict__.values():
                    try:
                        if issubclass(item, pyrestful.rest.RestHandler):
                            self.handlers.append(item)
                    except TypeError:
                        pass

    @staticmethod
    def is_python_module(directory):
        """ 判断是否python模块：含有__init__.py文件的目录 """
        if '__init__.py' in os.listdir(directory):
            return True
        else:
            return False

    @staticmethod
    def is_python_file(f):
        """ 判断是否python文件：后缀以.py结尾的文件 """
        if f.endswith('.py'):
            return True
        else:
            return False