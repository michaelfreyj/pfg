# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import sys

from .config_utils import make_pfgrc, make_template_dir

from . import __version__

# __version__ = '0.0.1'

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
    parser = argparse.ArgumentParser(
            prog="pfg",
            description="Generates a new file from a skeleton",
            usage="""\
\t%(prog)s [-t FILE] [-i FILE | --save_yaml] [-o FILE] [-p] [-q | -v | -d]
\t%(prog)s -c | --config
\t%(prog)s -h | --help
\t%(prog)s -V | --version""",
            # epilog="For more options, ask me",
            )
    verbosity = parser.add_mutually_exclusive_group()
    yaml = parser.add_mutually_exclusive_group()
    parser.add_argument(
            "-V", "--version", action="version",
            version=f"PythonFileGenerator {__version__}",
            help="display version number"
            )
    parser.add_argument(
            "-t", "--template", nargs=1, action="store",
            metavar="F",
            help="specify template file to use",
            )
    parser.add_argument(
            "-o", "--out", nargs=1, dest="outfile", action="store",
            metavar="F",
            help="name for output file",
            )
    parser.add_argument(
            "-p", "--print", dest="print_to_console", action="store_true",
            help="print output to console",
            )
    yaml.add_argument(
            "-i", "--in", nargs=1, dest="infile", action="store",
            metavar="F",
            help="load yaml file to generate file non-interactively",
            )
    yaml.add_argument(
            "--save_yaml", dest="yaml", action="store_true",
            help="save yaml dict for future use",
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
    # parser.add_argument(
    #         "-l", "--log", action="store_true", default=False, 
    #         help="write log to file",
    #         )
    # parser.add_argument(
    #         "--tree", action=TreeAction,
    #         help="create a directory tree with or without files in it"
    #         )
    parser.add_argument(
            "--config", nargs=0, action=ConfigAction,
            help="run app configuration tool",
            )
    return parser
# }}}

def set_loggers(args):# {{{
    """Creates logger objects for the header and body"""
    # create logger objects
    logger = logging.getLogger('pfg')
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    logger.setLevel(args.log_level)
    ch.setLevel(args.log_level)
    # set formatting for logger
    formatter = logging.Formatter('{levelname:<7}: {message}', style="{")
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


class ConfigAction(argparse.Action):
    # def __init__(self, option_strings, dest, nargs=None, **kwargs):
    #     if nargs is not None:
    #         raise ValueError("nargs not allowed")
    #     super(ConfigAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        make_pfgrc()
        print('----------------------------------------')
        make_template_dir() 
        sys.exit(0)
