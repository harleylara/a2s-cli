from argparse import ArgumentParser, Namespace
from a2s.commands import Command
from a2s.config import SUPPORTED_ROBOTS

class Ls(Command):
    """
    List all the supported robots.
    """

    def add_arguments(self, parser: ArgumentParser):
        pass

    def execute(self, args: Namespace):
        print("List of supported robots:")
        for robot in SUPPORTED_ROBOTS:
            print(f" - {robot}")
