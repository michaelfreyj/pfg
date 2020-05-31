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

def choice(opts): # {{{
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
# }}}

def yes_or_no(message):# {{{
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
# }}}

def set_arguments():# {{{
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
            "--config", help="generate and write config for for pytemplate",
            )
    parser.add_argument(
            "-t", "--template", action="store", metavar="FILE",
            help="specify template file to use",
            )
    parser.add_argument(
            "-i", "--in", nargs=1, dest="infile", action="store", metavar="FILE",
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
# }}}

def set_loggers(args):# {{{
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
# }}}

