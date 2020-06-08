#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this is to generate a config file when the --config flag is passed

from configparser import ConfigParser
import logging
from pathlib import Path

from .input_utils import choice, yes_or_no

log = logging.getLogger('pfg.config')
log.addHandler(logging.NullHandler())

home = Path.home()

def make_pfgrc():
    config = home.joinpath(".config/pfg/pfgrc")
    if config.exists():
        if config.is_file():
            if yes_or_no("a pfgrc file exists. overwrite the old one?"):
                config.touch
        else:
            print(f'{config} exists and is not a file')
    else:
        if yes_or_no("make pfgrc at \'{config}\'"):
            try:
                config.parent.mkdir()
                print(f'creating \'{config.parent}\'')
            except FileExistsError:
                print(f'\'{config.parent}\' exists')
            print('writing \'pfgrc\'')
            config.touch
        else:
            print('not creating \'pfgrc\' file')
    print()
            # actually write file.. in the future


def make_template_dir():
    template_dir = home.joinpath(".config/pfg/templates")
    print('checking if a template folder exists')
    print()
    if template_dir.exists():
        print('a folder for custom templates already exists')
        print(f'here -> \'{template_dir}\'')
    else:
        print('no template folder found')
        if yes_or_no(f'create \'{template_dir}\'?'):
            print(f'creating template folder at \'{template_dir}\'')
            template_dir.mkdir(parents=True)
            # move sample.fgt here to reference
        
