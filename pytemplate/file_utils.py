# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
# import datetime
import importlib
import logging
# import os
# from pkgutil
# import sys
import time
import yaml

log = logging.getLogger('pytemplate.methods').addHandler(logging.NullHandler())
now = time.localtime()

def read_file(filename): # v1
    with open(filename, 'r') as f:
        data = f.read()
    yaml_text = data.split('^^^\n')[0]
    template = data.split('^^^\n')[1]
    return (yaml_text, template)


# def load_yaml(filename): # incomplete
#     with open(filename, 'r') as f:
#         try:
#             data = yaml.load(f )
#              data = list(ya ml.load_all(f, Loader=yaml.FullLoader))

# def write(template_file):
#     dummy3 =1

