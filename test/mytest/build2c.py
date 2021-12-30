#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
@author: Ch3nYe
@license: GPL
@contact: sud0su@qq.com
@file: build2c.py
@date: 2021/12/30 18:59
@desc: 
@usage:
"""

import Cython.Build
import distutils.core


def py2c(file):
    cpy = Cython.Build.cythonize(file)  # 返回distutils.extension.Extension对象列表

    distutils.core.setup(
        name='pyd的编译',  # 包名称
        version="0.0.1",  # 包版本号
        ext_modules=cpy,  # 扩展模块
        author="Ch3nYe",  # 作者
        author_email='test@test.com'  # 作者邮箱
    )


if __name__ == '__main__':
    file = "../mytest2/test.py"
    py2c(file)