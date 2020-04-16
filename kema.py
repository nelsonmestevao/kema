#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Kema.

Usage:
  kema ship new <name>...
  kema ship <name> move <x> <y> [--speed=<kn>]
  kema ship shoot <x> <y>
  kema mine (set|remove) <x> <y> [--moored | --drifting]
  kema (-h | --help)
  kema --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""
from docopt import docopt
import configparser

from string import Template

# config = configparser.ConfigParser()
# config.read("config.ini")

# template_header = Template(open("templates/header.tmpl.h").read())
# template_source = Template(open("templates/source.tmpl.c").read())

# module = {"name": "content"}

# with open(f'{config["headers"]["dir"]}/{module["name"]}.h', "w") as out:
#     out.write(template_header.substitute(module=module["name"].upper()))

# with open(f'{config["source"]["dir"]}/{module["name"]}.c', "w") as out:
#     out.write(template_source.substitute(module=module["name"]))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Kema 0.1.0')
    print(arguments)
