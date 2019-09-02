#!/usr/bin/ python
# -*- coding:utf-8 -*-
# @Time : 2019/8/30 16:41
# @Author : YingHuang

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def element_error(self):
        return repr(self.value)