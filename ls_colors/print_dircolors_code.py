#!/usr/bin/python3
"""
Modify system environment to colorize ls based on file extensions

Call this script with the arguments to ls
Eg. print_dircolors_code.py -al my/folder

Conventions:
dircolors - output from `dircolors -p` + our extensions
dircolors_code - shell code needed to modify environment
"""

from sys import argv
from tempfile import NamedTemporaryFile
from subprocess import check_output, CalledProcessError

from extension_to_color import get_extension_to_color


def format_ext(ext, color):
    """
    Format ext to add to `dircolors -p`

    >>> format_ext('txt', '33')
    .txt 00:33\n

    :return: str
    """
    return '.{ext} 00;{color}\n'.format(ext=ext, color=color)


def get_dircolors(ext_to_color):
    """
    Run `dircolors -p` and add the given extensions to the output

    :return: str
    """
    return check_output(['dircolors'] + ['-p']).decode('utf-8') + \
           ''.join(format_ext(ext, color) for ext, color in ext_to_color.items())


def get_dircolors_code_from_file(filename):
    """
    Get shell code by running `dircolors -b` on filename

    :param filename: str
    :return: shell code
    """
    return check_output(['dircolors'] + ['-b'] + [filename]).decode('utf-8')


def write_dircolors_to_file(dircolors):
    """
    :param dircolors: str
    :return: filename
    """
    tmp = NamedTemporaryFile(mode='w+t', delete=False)
    tmp.write(dircolors)
    tmp.close()

    return tmp.name


def get_dircolors_code(dircolors):
    """
    :param dircolors: str
    :return: shell code
    """
    file = write_dircolors_to_file(dircolors)

    dircolors_code = get_dircolors_code_from_file(file)
    return dircolors_code


def print_dircolors_code(ls_args):
    ext_to_color = get_extension_to_color(ls_args)

    # dircolors is the output of `dircolors -p` along with out custom extensions
    dircolors = get_dircolors(ext_to_color)

    # dircolors_code is shell code used to modify our environment
    print(get_dircolors_code(dircolors))


if __name__ == '__main__':
    try:
        print_dircolors_code(argv[1:])
    # If the arguments to ls are bad, then we get a CalledProcessError
    # In that case, do nothing to the environment and let the call to `ls` handle it
    except CalledProcessError:
        pass
