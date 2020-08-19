#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Kema.

Usage:
  kema [options] (generate | gen | g) <name>...
  kema (-h | --help)
  kema --version

Options:
  -h --help         Show this screen.
  -v --version      Show version.
  -l --lang=<lang>  Choose programming language [default: C].
  -d --debug        Run in debug mode for developting purposes.

"""
from string import Template
import configparser
import os

from docopt import docopt  # type: ignore

from kema import VERSION

DEBUG = False


def get_config_path() -> str:
    """TODO
    :returns: TODO
    """
    if DEBUG:
        return "data"

    home_path = os.path.expanduser("~")
    return os.path.join(home_path, ".config", "kema")


def get_config() -> str:
    """TODO: Docstring for get_config.
    :returns: TODO

    """
    return os.path.join(get_config_path(), "kema.ini")


def get_template(template: str) -> str:
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

    if DEBUG:
        print("ARGV:", arguments)

    config = configparser.ConfigParser()
    config.read(get_config())

    template_header = Template(
        open(get_template(config["C.headers"]["template"])).read())

    template_source = Template(
        open(get_template(config["C.source"]["template"])).read())

    if arguments["generate"] or arguments["gen"] or arguments["g"]:
        os.makedirs(config["C.headers"]["dir"], exist_ok=True)
        os.makedirs(config["C.source"]["dir"], exist_ok=True)

        if not arguments["--lang"] == "C":
            return

        for module in arguments["<name>"]:
            with open(f'{config["C.headers"]["dir"]}/{module}.h', "w") as out:
                out.write(template_header.substitute(module=module.upper()))

            with open(f'{config["C.source"]["dir"]}/{module}.c', "w") as out:
                out.write(template_source.substitute(module=module))


if __name__ == "__main__":
    DEBUG = docopt(__doc__, version=f"Kema {VERSION}")["--debug"]
    main()
