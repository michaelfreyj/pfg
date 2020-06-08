# vim:fdm=marker
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import logging
# import os
from pathlib import Path
# from pkgutil
# import sys
import yaml

log = logging.getLogger('pfg.file_utils')
log.addHandler(logging.NullHandler())
home = Path.home()

