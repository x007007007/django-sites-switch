#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from setuptools import setup, find_packages
import versioneer


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with open(filename) as fp:
        return fp.read()

setup(
    name='django-sites-switch',
    version=versioneer.get_version(),
    description='let django.contrib.sites object automatically switch by http request',
    long_description=read('README.md'),
    keywords=['django', 'sites',  'request'],
    author='Xingci Xu',
    author_email='x007007007@hotmail.com',
    package_dir={
        "": "src"
    },
    url="https://github.com/x007007007/django-sites-switch",
    download_url="https://github.com/x007007007/django-sites-switch/archive/master.zip",
    license='MIT',
    packages=find_packages("src"),
    package_data={
        '': [],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    install_requires=[],
    cmdclass=versioneer.get_cmdclass(),
)
