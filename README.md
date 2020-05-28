pytemplate
==========
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
- [ ] leave out or include options sections
- [ ] loop sections for defining repetitive things (command line options)


Installation
------------

Once v1.0 is released, this section will be populated..

Decide on pip or installation script

Usage
-----

```
usage: pytemplate [options]

Generates a new file from a skeleton

optional arguments:
  -h, --help           show this help message and exit
    -i FILE, --in FILE   specify yaml file to generate file non-interactively
    -o FILE, --out FILE  specify name for output file (default=title)
    -l, --log            write log to file
    -q, --quiet          quiet output
    -v, --verbose        Verbose output
    -d, --debug          create debugging log
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
- [ ] pip setup.py

Making custom templates
-----------------------

Any variable that is to be replaced is written
`%%My-Variable%%` where `My-Variable` is the name of your variable

Optional sections are indicated by placing `***My-Section***` and
`+++My-Section+++` on the lines before and after the section, respectively, where `My-Section` is the name of your section.


Once v1.0 is released, this section will be populated..


To-Do
-----

- [ ] GUI menu
- [ ] ncurses interface
- [ ] console interface
- [ ] Arguments
    - [x] `-h/--help`       print help menu
    - [ ] `-g/--gui`        launch gui
    - [ ] `-n/--ncurses`    launch gui
    - [ ] `--config`        create application config file 
    - [ ] `-l/--log`        output log messages to logfile (optionally takes arg)
    - [ ] `-t/--template`   specify file location of template to use (nargs=1)
    - [ ] `-i/--in`         specify yaml file with variables (nargs=1)
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
    - [ ] generate application config file
    - [x] creating argument parser
    - [x] creating loggers
    - [x] multiple choice selection
    - [x] yes/no selection
    - [ ] checking for built-in templates
    - [ ] checking for custom templates
    - [ ] read built-in template
    - [x] read custom template
    - [x] split template file into yaml and template text
    - [x] interpret yaml file
    - [x] query user for inputs to define yaml-dict interactively
    - [ ] read non-interactive user defined yaml file into yaml-dict
    - [x] use yaml-dict to substitute
    - [ ] write skeleton to file
- [ ] create templates
- [ ] read application config file for settings if available
    - [ ] include built-in templates in choice
- [ ] author info
- [ ] always/never use todays date
- [ ] 
- [ ] ability to loop on section (for defining multiples of something repetitive)
