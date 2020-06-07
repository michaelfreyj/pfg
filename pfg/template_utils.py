# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import importlib
import logging
# import os
from pathlib import Path
# from pkgutil
# import sys
import time
import yaml

from input_utils import yes_or_no, choice

log = logging.getLogger('pfg.template_utils')
log.addHandler(logging.NullHandler())
now = time.localtime()

home = Path.home()
template_dirs = [
        ".config/pfg/templates",
        ".pfg/templates",
        ""
        ]


Template = namedtuple('Template', ['name', 'path'])

def check_templates():
    builtin_list = []
    custom_list = []
    # builtin templates
    # Import templates that ship with the package and send itttttt
    # custom templates
    for directory in template_dirs:
        temp_dir = home.joinpath(directory)
        if temp_dir.exists():
            if temp_dir.is_dir():
                log.debug(f"searching for templates in \'{temp_dir}\'")
                templates = list(temp_dir.glob("*.fgt"))
                for t in templates:
                    custom_list.append(Template(t.stem + " (custom)", t))
            else:
                log.debug(f"\'{temp_dir}\' exists, but is not a directory")
        else:
            log.debug(f"\'{temp_dir}\' does not exist")
    if len(builtin_list) == 0:
        log.info('no built-in templates found')
    if len(custom_list) == 0:
        log.info('no custom templates found')
    template_list = builtin_list + custom_list
    log.debug('templates found')
    for t in template_list:
        log.debug(f'|--->\'{t.name}\'')
    return template_list



def parse_yaml(yaml_text): # incomplete{{{
    substitutions = {}
    for i, section in enumerate(yaml_text.split('---\n')):
        sec = yaml.load(section, Loader=yaml.FullLoader)
        if i == 0:
            try:
                extension = sec['extension']
                log.info(f'file extension is \'{sec["extension"]}\'')
            except (KeyError, TypeError):
                log.warning('extension not defined in template file')
                log.warning('setting default to \'.txt\'')
                extension = 'txt'
            try:
                substitutions.update({ 'required' : {} })
                for item in sec['required']:
                    substitutions['required'].update({ item : None })
                log.info('list of required replacements:')
                log.info(sec['required'])
            except KeyError:
                log.error('no required fields defined in template...')
                raise
                log.error('using values \'title\', \'author\', \'date\'')
                substitutions['required'].update(
                        { "title" : None, "author" : None, "date" : None }
                        )
        elif i == 1:
            for key, value in sec.items():
                substitutions.update({ key : { "include" : True }})
                for item in value:
                    substitutions[key].update({ item : None })

    return substitutions, extension
# }}}

def query(subs):# {{{
    """Defines a set of substitutions for a template"""
    for sec, subdict in subs.items():
        if sec == "extension":
            pass
        elif sec == 'required':
            for key, value in subdict.items():
                if key == "date":
                    if yes_or_no('Use today\'s date?'):
                        date = f'{now.tm_year}-{now.tm_mon}-{now.tm_mday}'
                        subs[sec].update({ key : date })
                    else:
                        subs[sec].update(
                                { key : input(f'{key} >> ')})
                else:
                    subs[sec].update(
                            { key : input(f'{key} >> ')})
        else:
            for key, value in subdict.items():
                if subdict['include']:
                    if key == 'include':
                        subs[sec].update(
                                { key : yes_or_no(
                                    f'Include {sec} section?') })
                    else:
                        subs[sec].update(
                                { key : input(f'{key} >> ')})

    # return subs
# }}}

def substitute(template, subs):# {{{
    """Defines a set of substitutions for a template"""
    for sec, subdict in subs.items():
        if sec == 'required':
            for key, value in subdict.items():
                template = value.join(template.split(f'%%{key}%%'))
        else:
            if subdict['include']:
                for key, value in subdict.items():
                    if key != 'include':
                        template = value.join(template.split(f'%%{key}%%'))
                    else:
                        pass
            else:
                # Keep text before and after optional section
                print(f'removing {sec} section from the file')
                template = template.split(f'***{sec}***\n')[0] + \
                        template.split(f'\n+++{sec}+++')[1]
    return template
# }}}

