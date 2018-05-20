#!/usr/bin/env python
# coding=utf-8
try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Lyndon',
    'url': '',
    'download_url': '',
    'author_email': 'hello@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['game'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
