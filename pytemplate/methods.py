#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys
from pkgutil 

def choice(opts):
    """prints a a list of options out, returns selected option
    
    Parameters
    ----------
    opts: list
        list of options to print

    Returns
    -------
    selected: 
    """
    selected = False
    for i, n in enumerate(opts):
        print('{:.<6}{}'.format(i+1, n))
    print()
    while True:
        user_input = input('Enter your choice\n>> ')
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

def verbose_print(text, verbose):
    if verbose == True:
        print(text)
    else:
        pass

def load_available_templates():
    

def read_template(path):
    with open(path, 'r') as f:
        template = f.read()
    return lines


def get_keywords(template):
    """Parses file to get sections and keywords
    `%% keyword %% `
    `*** boolean ***`
    """
    temp_sections = template.split('***')
    boolean_sections = []
    keywords = []
    sections = []
    for sec, ind in enumerate(temp_sections):
        sections.append(sec.split('\n'))
        keywords.append({})
        for l in sections:
            temp_line = l.split('%%') 
            i = 1 
            for v in range(int((len( temp_line)-1)/2)): 
                keywords[-1].update( {temp_line[i] : None } ) 
                i += 2 

        if (i%2) == 1:
            # sets dict section name to section name
            boolean_sections.append(
                { "name" : sec.split('\n')[0], "include" : True })
        elif (i%2) == 0:
            boolean_sections.append(False)
        else:
            pass
    return sections, boolean_sections, keywords

def query(keywords, boolean_sections):
    for k, b in zip(keywords, boolean_sections):
        if b == False:
            for keys in k.items():
                value = str(input(f'{key} : '))
                k.update({key : value})
        elif b != False:
            while True:
            include = str(input(f'include {b["name"]}? [y]/n'))
            if include == "n" or include == "N":
                b.update({ "include" : False })
                break
            elif include == "y" or include == "Y" or include == "":
                for keys in k.items():
                    value = str(input(f'{key} : '))
                    k.update({key : value})
                break
            else:
                print(f'you entered \'{include}\' which is not valid')
                print('try again...')


def substitue_keywords()

def make_file(template_file, definitions):


