#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
    name = 'my_app',
    version = '1.0',
    license = 'GNU Geeneral Public License v3',
    author = 'Jiezhi',
    author_email = 'Jiezhi.G@gmail.com',
    description = 'Hello world application for Flask',
    packages = ['my_app'],
    platforms = 'any',
    install_requires=[
        'flask',
    ],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Prorgramming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
