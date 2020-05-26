#!/usr/bin/env python
# -*- coding: utf-8 -*-

requires = [
        'title',
        'author',
        'date',
        'summary',
        'getopts',
        ]

def make(fields):
    template = \
    f"""#!/usr/bin/env bash

    # ##################################################
    # TITLE: {title} 
    # AUTHOR: {author}
    # DATE: {date}
    # SUMMARY:{summary}
    # 
    version="1.0.0"               # Sets version variable
    #
    # HISTORY:
    #   2020-05-24  --  v.1.0.0 - Created
    #                   v.1.1.1 - Moved all shared variables to Utils
    #                           - Added $PASS variable when -p is passed
    #
    # ##################################################
    """


    """GetOpts
    while getopts ":ht" opt; do
      case ${opt} in
        h) # process option h
          ;;
        t) # process option t
          ;;
        \?) echo "Usage: cmd [-h] [-t]"
          ;;
      esac
    done
    """   

