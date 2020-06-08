# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
import logging
import os
from pathlib import Path
import sys
import time
import yaml

from .input_utils import choice, yes_or_no
from .template_utils import check_templates

log = logging.getLogger('pfg.Template')
log.addHandler(logging.NullHandler())
now = time.localtime()
home = Path.home()
cwd = Path.cwd()

class Template:
    def __init__(self, args):# {{{
        if args.outfile is not None:
            self.outfile = Path(args.outfile[0])
        elif args.outfile is None and not args.print_to_console:
            outfile = input("enter the name for file (no extension) to be created\n>> ")
            self.set_outfile(outfile)
        else:
            self.outfile = Path(
                    'dry-run_{}-{:02d}-{:02d}_{:02d}:{:02d}'.format(
                        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour,
                        now.tm_min,)
                    )
        if args.template is not None:
            path = Path(args.template[0])
            available_templates, names = check_templates()
            print(names)
            print(args.template[0])
            if args.template[0] in names:
                self.set_template_file(available_templates[names.index(args.template[0])])
            elif not path.exists():
                log.error(f'template \'{path}\' does not exist')
                sys.exit(1)
            elif not path.is_file():
                log.error(f'template \'{path}\' is not a file')
                sys.exit(1)
            else: 
                self.template_file = path
            self.read_template()
            self.parse_yaml()
        elif args.template is None:
            available_templates, names = check_templates()
            self.set_template_file(choice(available_templates))
            self.read_template()
            self.parse_yaml()
        if args.infile is not None:
            path = Path(args.infile[0])
            if not path.exists():
                log.error(f'yaml \'{path}\' does not exist')
                sys.exit(1)
            elif not path.is_file():
                log.error(f'yaml \'{path}\' is not a file')
                sys.exit(1)
            else: 
                self.infile = path
                self.read_yaml()
        elif args.infile is None:
            self.query()
        self.substitute()
        if args.print_to_console is True:
            self.print()
        else:
            self.write()
        if args.yaml is True:
            self.save_yaml()
        self.rc = None
    # }}}

    def set_outfile(self, filepath):# {{{
        self.outfile = Path(filepath)
    # }}}

    def set_infile(self, filepath):# {{{
        self.infile = Path(filepath)
    # }}}

    def set_template_file(self, filepath):# {{{
        self.template_file = Path(filepath)
    # }}}

    def read_rc(self):# {{{
        dummy = 1
        config_locations = [
                home.joinpath(".config/pfg"),
                home.joinpath(".pfg")
                ]
    # }}}

    def read_template(self):# {{{
        log.info(f'reading template text from \'{self.template_file}\'')
        data = self.template_file.read_text()
        self.yaml_text = data.split('^^^\n')[0]
        self.template = data.split('^^^\n')[1]
    # }}}

    def read_yaml(self):# {{{
        data = self.infile.read_text()
        log.info(f'loading yaml dictionary from \'{self.infile}\'')
        self.subs = yaml.load(data, Loader=yaml.FullLoader)
    # }}}

    def parse_yaml(self): # {{{
        keyword_dict = {}
        for i, section in enumerate(self.yaml_text.split('---\n')):
            sec = yaml.load(section, Loader=yaml.FullLoader)
            if i == 0:
                try:
                    extension = sec['extension']
                    log.info(f'file extension is \'{sec["extension"]}\'')
                except (KeyError, TypeError):
                    log.warning('extension not defined in template file')
                    log.warning('setting default to \'.txt\'')
                    extension = '.txt'
                try:
                    keyword_dict.update({ 'required' : {} })
                    for item in sec['required']:
                        keyword_dict['required'].update({ item : None })
                    log.info('list of required replacements:')
                    log.info(sec['required'])
                except KeyError:
                    log.error('no required fields defined in template...')
                    raise
                    log.error('using values \'title\', \'author\', \'date\'')
                    keyword_dict['required'].update(
                            { "title" : None, "author" : None, "date" : None }
                            )
            elif i == 1:
                for key, value in sec.items():
                    keyword_dict.update({ key : { "include" : True }})
                    for item in value:
                        keyword_dict[key].update({ item : None })
        self.dict = keyword_dict
        self.extension = extension
        self.outfile = self.outfile.with_suffix(extension)
    # }}}

    def query(self):# {{{
        """Defines a set of substitutions for a template"""
        self.subs = deepcopy(keyword_dict)
        for sec, subdict in self.dict.items():
            if sec == "extension":
                pass
            elif sec == 'required':
                for key, value in subdict.items():
                    if key == "date":
                        if yes_or_no('Use today\'s date?'):
                            date = f'{now.tm_year}-{now.tm_mon}-{now.tm_mday}'
                            self.subs[sec].update({ key : date })
                        else:
                            self.subs[sec].update(
                                    { key : input(f'{key} >> ')})
                    else:
                        self.subs[sec].update(
                                { key : input(f'{key} >> ')})
            else:
                for key, value in subdict.items():
                    if subdict['include']:
                        if key == 'include':
                            self.subs[sec].update(
                                    { key : yes_or_no(
                                        f'Include {sec} section?') })
                        else:
                            self.subs[sec].update(
                                    { key : input(f'{key} >> ')})
    # }}}

    def substitute(self):# {{{
        """Defines a set of substitutions for a template"""
        template = self.template
        for sec, subdict in self.subs.items():
            if sec == 'required':
                for key, value in subdict.items():
                    template = value.join(template.split(f'%%{key}%%'))
            else:
                if subdict['include']:
                    template = ''.join(template.split(f'***{sec}***\n'))
                    template = ''.join(template.split(f'\n+++{sec}+++'))
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
        self.template_final = template
    # }}}

    def print(self):# {{{
        print('{:#^79}'.format(''))
        print('#{:^77}#'.format('Begin Template'))
        print('{:#^79}'.format(''))
        print(self.template_final)
        print('{:#^79}'.format(''))
        print('#{:^77}#'.format('End Template'))
        print('{:#^79}'.format(''))
        log.debug(f'substitutions dict:\n{yaml.dump(self.subs)}')
    # }}}

def save_yaml(self):# {{{
    path = input('enter a name for the yaml dict') + '.yml'
    log.info('saving dictionary to \'{path}\'')
    yaml.dump(self.subs, open(path))
    # }}}

    def write(self):# {{{
        write = True
        log.debug(f'file path: {self.outfile}')
        if self.outfile.exists():
            write = yes_or_no(f'\'{self.outfile.name}\' already exists, overwrite it?')
        if not write:
            if yes_or_no('do you want to change the name/path of the file?'):
                new_path = input('enter the new name/path >> ')
                self.set_outfile(new_path)
        elif write:
            if not self.outfile.parent.exists():
                log.info(f'creating \'{self.outfile.parent}\'')
                self.outfile.parent.mkdir(parents=True)
            log.info(f'writing \'{self.outfile.name}\' to \'{self.outfile.parent}\'')
            self.outfile.write_text(self.template)
        else:
            log.info(f'\'{self.outfile.name}\' was not written')
    # }}}
