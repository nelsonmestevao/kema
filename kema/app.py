#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Kema.

Usage:
  kema new <name>...
  kema (-h | --help)
  kema --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from string import Template
import configparser
import os

from docopt import docopt

from kema import VERSION


def get_config_path():
    """TODO
    :returns: TODO
    """
    home_path = os.path.expanduser("~")
    return os.path.join(home_path, ".config", "kema")


def get_config():
    """TODO: Docstring for get_config.
    :returns: TODO

    """
    return os.path.join(get_config_path(), "kema.ini")


def get_template(template):
    """TODO
    :returns: TODO
    """
    templates_dir = os.path.join(get_config_path(), "templates")
    return os.path.join(templates_dir, template)


def main():
    """
    Main entry point for the tool.
    """
    arguments = docopt(__doc__, version=f"Kema {VERSION}")

    config = configparser.ConfigParser()
    config.read(get_config())

    template_header = Template(open(get_template("header.tmpl.h")).read())
    template_source = Template(open(get_template("source.tmpl.c")).read())

    if arguments["new"]:
        os.makedirs(config["headers"]["dir"])
        os.makedirs(config["source"]["dir"])

        for module in arguments["<name>"]:
            with open(f'{config["headers"]["dir"]}/{module}.h', "w") as out:
                out.write(template_header.substitute(module=module.upper()))

            with open(f'{config["source"]["dir"]}/{module}.c', "w") as out:
                out.write(template_source.substitute(module=module))


if __name__ == "__main__":
    print(os.path.abspath(os.path.dirname(__file__)))
    main()
