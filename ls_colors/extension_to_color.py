#!/usr/bin/python3
"""
Associate a color with each extension in the requested directory
"""

from hashlib import md5
from subprocess import check_output, DEVNULL
from json import load
from os.path import abspath, join, dirname


# Where to get the colour codes for ls
COLORS_FILE = 'colors.json'
# ./COLORS_FILE
COLORS = load(open(join(dirname(abspath(__file__)), 'colors.json')))['colors']


def get_ls_lines(ls_args):
    """
    Get output from ls

    Suppresses error output

    >>> get_ls_lines(get_ls_lines(['-al', 'my/folder'])
    ['file.cc', 'file.h']

    :param ls_args: list of str
    :return: list of str
    :raises: CalledProcessError
    """
    return check_output(['ls'] + ls_args, stderr=DEVNULL).decode('utf-8').splitlines()


def get_ext(filename):
    """Get a filename's extension"""
    return filename.split('.')[-1]


def has_ext(filename):
    return '.' in filename and not filename.startswith('.')


def get_extensions(ls_args):
    """
    Get the file extensions given an ls query

    :param ls_args: list
    :return: set
    """
    return {get_ext(line) for line in get_ls_lines(ls_args) if has_ext(line)}


def get_color(extension):
    """
    Hash extension and return the appropriate colour

    :param extension: str
    :return: str
    """
    return COLORS[int(md5(extension.encode()).hexdigest(), 16) % len(COLORS)]


def get_extension_to_color(ls_args):
    """
    Takes the 'ls' command list, and returns a dict
    mapping from extension to a colour

    :param ls_args: list
    :return: {str -> int}
    """
    return {ext: get_color(ext) for ext in get_extensions(ls_args)}
