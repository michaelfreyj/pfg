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

log = logging.getLogger('pytemplate.methods')
now = time.localtime()

def choice(opts):
    """prints a a list of options out, returns selected option
    
    Parameters
    ----------
    opts: list
        list of options to print

    Returns
    -------
    selected: int
        index of the selected option
    """
    selected = False
    for i, n in enumerate(opts):
        print('{:.<6}{}'.format(i+1, n))
    print()
    while True:
        user_input = input('>> ')
        try:
            selection = opts[int(user_input)-1]
            break
        except (ValueError, IndexError):
            print('{:-^35}'.format(''))
            print('your entered {} which is not a valid option'.format(
                user_input))
            print('valid entries are integer values between 1 and {}'.format(
                len(opts)))
            print('{:-^35}'.format(''))
    return selection


def yes_or_no(message):
    """prompt for yes or no questions, default is yes
    """
    ans = input(message + ' [y]/n >> ')
    no = ['n', 'N', 'no', 'NO', 'No']
    yes = ['y', 'Y', 'yes', 'YES', 'Yes', '', ' ']
    while True:
        if ans in yes:
            return True
        elif ans in no:
            return False
        else:
            print(f'{ans} is not a valid answer')
            ans = input('[y]/n >> ')


def set_arguments():
    """Sets arguments for the command line interface
    """
    ## Logging levels
    # CRITICAL = 50
    # ERROR    = 40
    # WARNING  = 30
    # INFO     = 20
    # DEBUG    = 10
    # NOTSET   = 0
    parser = ArgumentParser(
            prog="pytemplate", description="Generates a new file from a skeleton",
            usage="pytemplate [options]", epilog="For more options, ask me"
            )
    verbosity = parser.add_mutually_exclusive_group()

    parser.add_argument(
            "-c", "--conf", nargs=1, dest="infile", action="store", metavar="FILE",
            help="specify yaml file to generate file non-interactively",
            )
    parser.add_argument(
            "-o", "--out", nargs=1, dest="outfile", action="store", metavar="FILE",
            help="specify name for output file (default=title)",
            )
    parser.add_argument(
            "-l", "--log", action="store_true", default=False, 
            help="write log to file",
            )
    verbosity.add_argument(
            "-q", "--quiet", dest="log_level", action="store_const", default=30,
            const=logging.CRITICAL, help="quiet output",
            )
    verbosity.add_argument(
            "-v", "--verbose", dest="log_level", action="store_const", default=30,
            const=logging.INFO, help="Verbose output",
            )
    verbosity.add_argument(
            "-d", "--debug", dest="log_level", action="store_const", default=30,
            const=logging.DEBUG, help="create debugging log",
            )
    return parser


def set_loggers(args):
    """Creates logger objects for the header and body"""
    # create logger objects
    logger = logging.getLogger('pytemplate')
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    logger.setLevel(args.log_level)
    ch.setLevel(args.log_level)
    # set formatting for logger
    formatter = logging.Formatter('{levelname}: {message}', style="{")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    # create logger for header specifically (is this dumb?)
    heading = logging.getLogger('heading')
    heading.setLevel(args.log_level)
    heading_ch = logging.StreamHandler()
    heading_ch.setLevel(args.log_level)
    heading_ch.setFormatter(logging.Formatter('{message}', style='{'))
    heading.addHandler(heading_ch)
    
    return logger, heading

# def check_for_templates():
#     dummy = 1

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


def parse_yaml(yaml_text): # incomplete
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


def query(subs):
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


def substitute(template, subs):
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

# def get_keywords(template):
#     """Parses file to get sections and keywords
#     `%% keyword %% `
#     `*** boolean ***`
#     """
#     temp_sections = template.split('***')
#     boolean_sections = []
#     keywords = []
#     sections = []
#     for sec, ind in enumerate(temp_sections):
#         sections.append(sec.split('\n'))
#         keywords.append({})
#         for l in sections:
#             temp_line = l.split('%%') 
#             i = 1 
#             for v in range(int((len( temp_line)-1)/2)): 
#                 keywords[-1].update( {temp_line[i] : None } ) 
#                 i += 2 

#         if (i%2) == 1:
#             # sets dict section name to section name
#             boolean_sections.append(
#                 { "name" : sec.split('\n')[0], "include" : True })
#         elif (i%2) == 0:
#             boolean_sections.append(False)
#         else:
#             pass
#     return sections, boolean_sections, keywords


# def query(keywords, boolean_sections):
#     for k, b in zip(keywords, boolean_sections):
#         if b == False:
#             for keys in k.items():
#                 value = str(input(f'{key} : '))
#                 k.update({key : value})
#         elif b != False:
#             while True:
#             include = str(input(f'include {b["name"]}? [y]/n'))
#             if include == "n" or include == "N":
#                 b.update({ "include" : False })
#                 break
#             elif include == "y" or include == "Y" or include == "":
#                 for keys in k.items():
#                     value = str(input(f'{key} : '))
#                     k.update({key : value})
#                 break
#             else:
#                 print(f'you entered \'{include}\' which is not valid')
#                 print('try again...')


# def write(template_file):
#     dummy3 =1

