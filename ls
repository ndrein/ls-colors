#!/usr/bin/python3
"""
Replacement for ls
"""
from os import system
from sys import stdout, argv
from colourize_ls import colourize_ls


def get_ls_args():
    return argv[1:]


def ls(args):
    system('ls {}'.format(args))


if stdout.isatty():
    args = get_ls_args()
    colourize_ls(args)
    ls(args)
