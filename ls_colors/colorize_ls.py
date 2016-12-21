#!/usr/bin/python3
"""
Modify system environment to colorize ls based on file extensions
"""

from os import remove, system
from tempfile import NamedTemporaryFile
from sys import exit
from subprocess import check_output, call

from extension_to_color import get_extension_to_color


def format_ext(ext, color):
    """
    Format ext to add to `dircolors -p`

    Eg.
    .txt 00;38

    :return: str
    """
    return '.{ext} 00;{color}\n'.format(ext=ext, color=color)


def get_dircolors(ext_to_color):
    """
    :return: str
    """
    return check_output('dircolors -p').decode('utf-8') + \
           ''.join(format_ext(ext, color) for ext, color in ext_to_color.items())


def get_dircolors_from_file(filename):
    call('dircolors -b {}'.format(filename))


def run_dircolors(dircolors):
    try:
        tmp = NamedTemporaryFile(mode='w+t', delete=False)
        tmp.write(dircolors)
        tmp.close()

        get_dircolors_from_file(tmp.name)

        remove(tmp.name)
    except FileNotFoundError:
        pass


def colourize_ls(ls_args):
    ext_to_color = get_extension_to_color(ls_args)
    run_dircolors(get_dircolors(ext_to_color))
