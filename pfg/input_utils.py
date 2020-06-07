# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import logging
import sys

log = logging.getLogger('pfg.input_utils')
log.addHandler(logging.NullHandler())


Template = namedtuple('Template', ['name', 'path'])

def choice(opts, message="select an option"): # {{{
    """prints a a list of options out, returns selected option
    
    Parameters
    ----------
    opts: list
        list of options to print

    message: string (optional)
        prompt to display

    Returns
    -------
    selection: int
        index of the selected option
    """
    if type(opts) == list:
        if len(opts) > 0:
            for i, n in enumerate(opts):
                log.debug(type(n))
                try:
                    print('{:<4}{}'.format(str(i+1)+'.', n.name))
                except AttributeError:
                    print('{:<4}{}'.format(str(i+1)+'.', n))
            print()
            while True:
                print(message)
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
        else:
            log.error('list of options contained zero items')
            sys.exit(1)
    else:
        log.error('options argument was not a list type')
        sys.exit(1)

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
            break
        elif ans in no:
            return False
            break
        else:
            print(f'{ans} is not a valid answer')
            ans = input('[y]/n >> ')
# }}}

