# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import logging
# import os
from pathlib import Path
# from pkgutil
# import sys
import yaml

log = logging.getLogger('pytemplate.file_utils')
log.addHandler(logging.NullHandler())
home = Path.home()

def read_template(filename): # v1
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

def read_yaml(filename):
    dummy = 1

def write_file(template, filepath):
    write = True
    log.debug(f'file path: {filepath}')
    if filepath.exists():
        write = yes_or_no(f'a file \'{filepath.name}\' already exists, overwrite it?')
    if write:
        filepath.write_text(template)
        log.info(f'\'{filepath.name}\' was written to \'{filepath.parent}\'')
    else:
        log.info(f'\'{filepath.name}\' was not written')

