#!/usr/bin/python3
"""
Modify system environment to colorize ls based on file extensions
"""

from sys import argv
from os import remove
from tempfile import NamedTemporaryFile
from subprocess import check_output, CalledProcessError

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
    return check_output(['dircolors'] + ['-p']).decode('utf-8') + \
           ''.join(format_ext(ext, color) for ext, color in ext_to_color.items())


def get_dircolors_from_file(filename):
    output = check_output(['dircolors'] + ['-b'] + [filename]).decode('utf-8')
    print(output)


def run_dircolors(dircolors):
    try:
        tmp = NamedTemporaryFile(mode='w+t', delete=False)
        tmp.write(dircolors)
        tmp.close()

        get_dircolors_from_file(tmp.name)

        remove(tmp.name)
    except FileNotFoundError:
        pass


def print_dircolors_code(ls_args):
    ext_to_color = get_extension_to_color(ls_args)
    run_dircolors(get_dircolors(ext_to_color))

if __name__ == '__main__':
    try:
        print_dircolors_code(argv[1:])
    # If the arguments to ls are bad, then we get a CalledProcessError
    # In that case, do nothing to the environment and let the call to `ls` handle it
    except CalledProcessError:
        pass
