#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pfg
----------



"""

from setuptools import setup, find_packages

import pfg

def read(filename):
    with open(filename) as f:
        return f.read()

setup(
    name='grip',
    version='4.5.2',
    description='Render local readme files before sending off to GitHub.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/grip',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'grip': ['static/*.*', 'static/octicons/*', 'templates/*']},
    install_requires=read('requirements.txt').splitlines(),
    extras_require={'tests': read('requirements-test.txt').splitlines()},
    zip_safe=False,
    entry_points={'console_scripts': ['grip = grip:main']},
)

setup(
    name="pfg",
    version="0.0.1",
    author="Michael J. Frey"
    author_email="michaelfreyj@gmail.com",
    description="Command line utility to quickly generate files from custom templates",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/michaelfreyj/pytemplate",
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'pytemplate' : 'templates/*'}
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
