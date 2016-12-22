#!/usr/bin/python3
"""
Associate a color with each extension in the requested directory
"""

from hashlib import md5
from subprocess import check_output, DEVNULL
from json import load
from os.path import abspath, join, dirname


COLORS_FILE = 'colors.json'
# ./COLORS_FILE
COLORS = load(open(join(dirname(abspath(__file__)), 'colors.json')))['colors']


def get_ls_lines(ls_args):
    return check_output(['ls'] + ls_args, stderr=DEVNULL).decode('utf-8').splitlines()


def get_ext(line):
    return line.split('.')[-1]


def has_ext(line):
    return '.' in line and not line.startswith('.')


def get_extensions(ls_args):
    return {get_ext(line) for line in get_ls_lines(ls_args) if has_ext(line)}


def get_color(extension):
    return COLORS[int(md5(extension.encode()).hexdigest(), 16) % len(COLORS)]


def get_extension_to_color(ls_args):
    """
    Takes the 'ls' command list, and returns a dict
    mapping from extension to a colour

    :param ls_args: list
    :return: {str -> int}
    """
    return {ext: get_color(ext) for ext in get_extensions(ls_args)}
