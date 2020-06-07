#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this is to generate a config file when the --config flag is passed

from input_utils import choice, yes_or_no
import logging
from pathlib import Path

log = logging.getLogger('pytemplate.config_utils')
log.addHandler(logging.NullHandler())

home = Path.home()

def make_rc():
    dummy = 1
    config_location = home.joinpath(".config/pytemplate")


def make_template_dir():
    dummy = 2


def read_rc():
    dummy = 1
    config_locations = [
            home.joinpath(".config/pytemplate"),
            home.joinpath(".pytemplate")
            ]
