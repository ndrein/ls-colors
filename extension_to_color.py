#!/usr/bin/python3
from subprocess import Popen, PIPE
from json import load
from command import Command


COLORS_FILE = 'colors.json'
COLORS = load(open('colors.json'))['colors']


def get_ls_lines(cmd_lst):
    return Command(cmd_lst).get_stdout_lines()


def get_ext(line):
    return line.split('.')[-1]


def has_ext(line):
    return '.' in line and not line.startswith('.')


def get_extensions(cmd_lst):
    return {get_ext(line) for line in get_ls_lines(cmd_lst) if has_ext(line)}


def get_color(extension):
    return COLORS[hash(extension) % len(COLORS)]


def get_extension_to_color(cmd_lst):
    return {ext: get_color(ext) for ext in get_extensions(cmd_lst)}
