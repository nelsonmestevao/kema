#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
from string import Template

config = configparser.ConfigParser()
config.read("config.ini")

template_header = Template(open("templates/header.tmpl.h").read())
template_source = Template(open("templates/source.tmpl.c").read())

module = {"name": "content"}

with open(f'{config["headers"]["dir"]}/{module["name"]}.h', "w") as out:
    out.write(template_header.substitute(module=module["name"].upper()))

with open(f'{config["source"]["dir"]}/{module["name"]}.c', "w") as out:
    out.write(template_source.substitute(module=module["name"]))
