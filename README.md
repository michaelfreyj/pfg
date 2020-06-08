Python File Generator
=====================
Command line utility to quickly generate files from custom templates

<!-- vim-markdown-toc GFM -->

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Available Templates](#available-templates)
* [Making custom templates](#making-custom-templates)
* [To-Do](#to-do)

<!-- vim-markdown-toc -->

Features
--------

- [ ] CLI operation
- [ ] generates a variety of templates
- [ ] non-interactive operation with yaml file
- [ ] custom templates can used, program with search in certain dirs for them
- [ ] simple variable substitutions
- [ ] include or exclude options sections
- [ ] loop sections for defining repetitive things (command line options)


Installation
------------

Once v1.0 is released, this section will be populated..

Decide on pip or installation script

Usage
-----

```
usage: 	pfg [-t FILE] [-i FILE] [-o FILE] [-p] [-q | -v | -d]
	pfg -c | --config
	pfg -h | --help
	pfg -V | --version

Generates a new file from a skeleton

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         display version number
  -t IN, --template IN  specify template file to use
  -i IN, --in IN        load yaml file to generate file non-interactively
  -o OUT, --out OUT     name for output file -- no file extension!
  -p, --print           print output to console
  -q, --quiet           quiet output
  -v, --verbose         Verbose output
  -d, --debug           create debugging log
  -c, --config          run app configuration tool
```

Once v1.0 is released, this section will be populated..

Available Templates
-------------------

- [ ] Latex doc
- [ ] LaTeX makefile
- [ ] Beamer presentation
- [ ] Beamer makefile
- [ ] makefile
- [ ] Bash script
- [ ] python script
- [ ] setup.py (for pip)
- [ ] Weekly report

Making custom templates
-----------------------

Any variable that is to be replaced is written
`%%My-Variable%%` where `My-Variable` is the name of your variable

Optional sections are indicated by placing `***My-Section***` and
`+++My-Section+++` on the lines before and after the section, respectively, where `My-Section` is the name of your section.


Once v1.0 is released, this section will be populated..


To-Do
-----

- [x] rename `pytemplate` to `pfg`
- [ ] GUI menu
- [ ] ncurses interface
- [ ] console interface
- [ ] Arguments
    - [x] `-h/--help`       print help menu
    - [x] `-V/--version`    print help menu
    - [ ] `-g/--gui`        launch gui
    - [ ] `-n/--ncurses`    launch gui
    - [x] `-c/--config`     run config tool 
    - [x] `-l/--log`        output log messages to logfile (optionally takes arg)
    - [x] `-t/--template`   specify file location of template to use (nargs=1)
    - [x] `-i/--in`         specify yaml file with variables (nargs=1)
    - [x] `-o/--out`        specify output file name (nargs=1)
    - [x] `-v/--verbose`    verbose outut
    - [x] `-q/--quiet`      quiet outut
    - [x] `-d/--debug`      debug outut
- [ ] use pip or installation script
    - [ ] installation script for streamlined installation
    - [ ] uninstall option in installation script...
- [ ] Loggers
    - [x] log
    - [x] heading
    - [ ] log to file based on args.log
    - [ ] log to console if args.log == False
    - [ ] implement dictConfig() to configure loggers and handlers
- [ ] functions
    - [x] custom config action that launchs config tool
    - [ ] configuration tool use [configparser](https://docs.python.org/3/library/configparser.html)
    - [x] creating argument parser
    - [x] creating loggers
    - [x] multiple choice selection
    - [x] yes/no selection
    - [ ] checking for built-in templates
    - [x] checking for custom templates
    - [ ] read built-in template
    - [x] read custom template
    - [x] split template file into yaml and template text
    - [x] interpret yaml file
    - [x] query user for inputs to define yaml-dict interactively
    - [ ] read non-interactive user defined yaml file into yaml-dict
    - [x] use yaml-dict to substitute
    - [ ] write skeleton to file
- [ ] wrap all template options into template class
- [ ] create templates (maybe even add template creation tool)
- [ ] read application config file for settings if available
    - [ ] include/exclude built-in templates in choice
    - [ ] 
    - [ ] author info
    - [ ] always/never use todays date
    - [ ] other config things
- [ ] ability to loop on section (for defining multiples of something repetitive)
- [ ] compile with pyinstaller for windows users (py2exe could work too)
- [ ] use travis to check builds
