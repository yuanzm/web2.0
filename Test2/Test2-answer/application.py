#!/usr/bin/env python
# coding=utf-8

from url import url 

import os.path
import tornado.web

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"template"),
    static_path=os.path.join(os.path.dirname(__file__),"static"),
    autoescape=None,
    debug=True,
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
)

application = tornado.web.Application(
    handlers=url,
    **setting
)
