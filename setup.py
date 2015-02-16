#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import woola
version = woola.__version__

setup(
    name='Woola',
    version=version,
    author="Derek Lin",
    author_email='derek.pc.lin@gmail.com',
    packages=[
        'woola',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['woola/manage.py'],
)
