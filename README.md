Python File Generator
=====================
Command line utility to quickly generate files from custom templates

<!-- vim-markdown-toc GFM -->

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Default Templates](#default-templates)
* [Making custom templates](#making-custom-templates)
* [Using non-interatice yaml files](#using-non-interatice-yaml-files)
* [Future Features](#future-features)
* [Future Templates](#future-templates)

<!-- vim-markdown-toc -->

Features
--------

- CLI operation
- simple variable substitutions
- include or exclude options sections
- non-interactive operation with yaml file
- save template substitutions as yaml file for future use to recreate that template
- custom templates can be put in `~/.config/pfg/templates`
- config file that defines prefences and frequent variables like `Author`

Installation
------------

Once v1.0 is released, this section will be populated..

- pip from github
- build from source (requires pyyaml)

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

Default Templates
-----------------

- example template

Certain templates are shipped with the program by default, but additional
templates I have made can be found in the pfg_templates dir. These can be
modified (if desired) and added to `~/.config/pfg/templates`.

Making custom templates
-----------------------

Any variable that is to be replaced is written
`%%My-Variable%%` where `My-Variable` is the name of your variable

Optional sections are indicated by placing `***My-Section***` and
`+++My-Section+++` on the lines before and after the section, respectively, where `My-Section` is the name of your section.

Any variable that is defined in the in the config file will be automatically substituted without asking.

Once v1.0 is released, this section will be populated..


Using non-interatice yaml files
-------------------------------

Once v1.0 is released, this section will be populated..

Future Features
---------------

- [ ] loop sections for defining repetitive things (command line options)
- [ ] config file generator
- [ ] template creation aid

Future Templates
----------------

- [ ] Latex doc
- [ ] LaTeX makefile
- [ ] Beamer presentation
- [ ] Beamer makefile
- [ ] C makefile
- [ ] Bash script
- [ ] python script
- [ ] matlab script
- [ ] setup.py (for pip)
- [ ] ansys journal file
- [ ] Weekly report
