# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import logging

# from . import __version__

__version__ = '0.0.1'

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
            prog="pytemplate",
            description="Generates a new file from a skeleton",
            usage="\t%(prog)s [options]\n\t%(prog)s -h | --help",
            epilog="For more options, ask me",
            )
    verbosity = parser.add_mutually_exclusive_group()
    parser.add_argument(
            "-V", "--version", action="version",
            version=f"%(prog)s v{__version__}",
            help="display version number"
            )
    parser.add_argument(
            "-t", "--template", action="store", metavar="FILE",
            help="specify template file to use",
            )
    parser.add_argument(
            "-i", "--in", nargs=1, dest="infile", action="store",
            metavar="FILE",
            help="load yaml file to generate file non-interactively",
            )
    parser.add_argument(
            "-o", "--out", nargs=1, dest="outfile", action="store",
            metavar="FILE",
            help="name for output file -- no file extension!",
            )
    parser.add_argument(
            "-p", "--print", dest="print_to_console", action="store_true",
            help="print output to console",
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
    #         "-c", "--config", action="store_true",
    #         help="run app configuration tool",
    #         )
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
    formatter = logging.Formatter('{levelname}:\t{message}', style="{")
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

