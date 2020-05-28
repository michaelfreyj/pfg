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

Any variable that is to be replaced is written
`%%My-Variable%%` where `My-Variable` is the name of your variable

Optional sections are indicated by placing `***My-Section***` and
`+++My-Section+++` on the lines before and after the section, respectively, where `My-Section` is the name of your section.


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


To-Do
-----

- [ ] GUI menu
- [ ] ncurses interface
- [ ] console interface
- [ ] Arguments
    - [x] (-h) help
    - [ ] (-g) gui
    - [ ] (-i) interactive
    - [ ] (-l) output log messages to logfile
    - [ ] (-t) specify file location of template to use
    - [ ] (-f) specify file with variables (yaml)
    - [x] (-o) specify output file name
    - [x] (-v) verbose outut
    - [x] (-q) quiet outut
    - [x] (-d) debug outut
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
- [ ] ability to loop on section (for defining multiples of something repetitive)
