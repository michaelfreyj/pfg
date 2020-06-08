#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pfg
----------
Command line utility to quickly generate files from custom templates

"""

from setuptools import setup, find_packages

def read(filename):
    with open(filename) as f:
        return f.read()

setup(
    name="pfg",
    version="0.0.1",
    author="Michael J. Frey",
    author_email="michaelfreyj@gmail.com",
    description="Command line utility to quickly generate files from custom templates",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/michaelfreyj/pytemplate",
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'pytemplate' : ['templates/*']},
    # install_requires=read('requirements.txt').splitlines(),
    # extras_require={'tests': read('requirements-test.txt').splitlines()},
    # entry_points={'console_scripts': ['grip = grip:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={'console_scripts' : ['pfg = pfg.__main__:main'],
    },
)
