#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys
import logging

log = logging.getLogger('pfg.methods')

def messages():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

def more_messages():
    logger.debug('another debug message')
    logger.info('another info message')
    logger.warning('another warn message')
    logger.error('another error message')
    logger.critical('another critical message')

