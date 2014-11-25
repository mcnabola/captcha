#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # python setup.py test
    import multiprocessing
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import captcha
from email.utils import parseaddr

author, author_email = parseaddr(captcha.__author__)
kwargs = {}


def fopen(filename):
    with open(filename) as f:
        return f.read()


setup(
    name='captcha',
    version=captcha.__version__,
    author=author,
    author_email=author_email,
    url=captcha.__homepage__,
    packages=['captcha'],
    description=captcha.__doc__,
    long_description=fopen('README.rst'),
    license='BSD',
    zip_safe=False,
    include_package_data=True,
    test_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    **kwargs
)