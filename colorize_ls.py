#!/usr/bin/python3
"""
Modify system environment to colourize ls based on file extensions
"""

from extension_to_color import get_extension_to_color
from command import Command


def format_ext(ext, color):
    """
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
            [format_ext(ext, color) for ext, color in ext_color.items()])
            

def save_to_dircolors_file(ext_to_color)
    with open


def colourize_ls(cmd_lst)
    dircolors = get_dircolors(get_extension_to_color(cmd_list))
    


