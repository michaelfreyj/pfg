#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
from pathlib import Path
import sys
import time
import yaml

from input_utils import choice
from sys_utils import set_arguments, set_loggers
from template_utils import check_templates
from template import Template
from test_methods import messages, more_messages

def main():
    parser = set_arguments()
    now = time.localtime()
    args = parser.parse_args()
    logger, heading = set_loggers(args)
    date_string = f'Date: {now.tm_year}-{now.tm_mon}-{now.tm_mday}'
    time_string = f'Time: {now.tm_hour}:{now.tm_min} {now.tm_zone}'
    head = "{3:-^50}\n{0: ^50}\n{1: ^50}\n\n{2: ^50}\n{3:-^50}\n".format(
            date_string, time_string, 'Begin build log', '',)
    heading.debug(head)
    logger.debug(args)

    if args.config:
        if logger.level > 20:
            logger.setLevel(logging.INFO)
        make_pfgrc()
        make_template_dir() 
        sys.exit(0)

    t = Template(args)
    if args.outfile == None:
        outfile = input("enter the name for file (no extension) to be created\n>> ")
        t.set_outfile(outfile)
    if args.template == None:
        available_templates = check_templates()
        t.set_template_file(choice(available_templates))
        t.read_template()
        t.parse_yaml()
    if args.infile is None:
        t.query()

    t.substitute()

    if args.print_to_console == True:
        print('{:#^79}'.format(''))
        print('#{:^77}#'.format('Begin Template'))
        print('{:#^79}'.format(''))
        t.print()
        print('{:#^79}'.format(''))
        print('#{:^77}#'.format('End Template'))
        print('{:#^79}'.format(''))
    else:
        t.write()
            
    logger.debug(f'Logger level = {args.log_level}')


if __name__ == '__main__':
    main()
