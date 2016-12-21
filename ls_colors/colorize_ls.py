#!/usr/bin/python3
"""
Modify system environment to colorize ls based on file extensions
"""

from tempfile import NamedTemporaryFile

from ls_colors.extension_to_color import get_extension_to_color
from ls_colors.command import Command


def format_ext(ext, color):
    """
    Format ext to add to `dircolors -p`

    Eg.
    .txt 00;38

    :return: str
    """
    return '.{ext} 00;{color}'.format(ext=ext, color=color)


def get_dircolors(ext_to_color):
    """
    :return: str
    """
    return '\n'.join(Command(['dircolors', '-p']).stdout_lines() + \
            [format_ext(ext, color) for ext, color in ext_to_color.items()])


def get_dircolors_from_file(filename):
    Command(['dircolors', '-b', filename]).run()


def run_dircolors(dircolors):
    tmp = NamedTemporaryFile(mode='w+t')
    try:
        tmp.write(dircolors)
        get_dircolors_from_file(tmp.name)
    finally:
        tmp.close()


def colourize_ls(cmd_lst):
    ext_to_color = get_extension_to_color(cmd_lst)
    run_dircolors(get_dircolors(ext_to_color))
