#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
@author: Ch3nYe
@license: GPL
@contact: sud0su@qq.com
@file: t1.py
@date: 2021/12/29 22:35
@desc: 
@usage: 
"""

from miasm.analysis.binary import Container
print(Container)

from core import myfunc_return_first_char
from core import sum_as_string
from core import __doc__

t = myfunc_return_first_char("ddd")
print(t)
print(sum_as_string(1232,21321))
print(__doc__)

from test import test_func
print(test_func(1,3))

from core import DummyClass
print(DummyClass.get_42())
