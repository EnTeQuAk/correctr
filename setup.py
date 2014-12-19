#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='correctr',
    version='0.1.0',
    description='yeah, whatever',
    long_description=read('README.rst'),
    author='Christopher Grebs',
    author_email='cg@webshox.org',
    url='https://github.com/EnTeQuAk/correctr',
    packages=find_packages(exclude=('tests',)),
    package_dir={
        'correctr': 'correctr'},
    include_package_data=True,
    install_requires=['TextBlob', 'pytest'],
    license="BSD",
    zip_safe=False,
    keywords='correctr',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'correctr = correctr:main',
        ]
    }
)
