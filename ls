#!/usr/bin/python3
"""
Replacement for ls
"""
from sys import stdout, argv
from colorize_ls import colourize_ls
from command import Command


def ls(args):
    Command(args).run()


if stdout.isatty():
    colourize_ls(argv)
    ls(argv)
