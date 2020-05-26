#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys
from pkgutil 

log = logging.getLogger('pytemplate.methods')

def messages():
    log.debug('this is a debug')
    log.info('this is info')
    log.warning('this is a warning')
    log.error('this is an error')
    log.critical('this is critical')
