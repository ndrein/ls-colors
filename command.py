#!/usr/bin/python3
from subprocess import Popen, PIPE


class Command:
    def __init__(self, command_list):
        """"
        :param command: str
        :param args: iterable of str
        """
        self.command_list = command_list

    def run(self):
        """
        Run command and return a pipe reference to Popen

        :return: pipe
        """
        return Popen(' '.join(self.command_list), shell=True, stdout=PIPE)

    def stdout_lines(self):
        """
        Return a generator of lines without whitespace
        """
        return (line.decode('utf-8').strip() for line in self.run().stdout)
