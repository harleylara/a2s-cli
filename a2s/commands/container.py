import subprocess
from argparse import ArgumentParser, Namespace
from a2s.commands import Command

class Container(Command):

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("robot", type=str.lower, choices=["nao", "nala"])

    def execute(self, args: Namespace):

        if args.robot == "nao":
            print("nao setup")
            subprocess.run(["apptainer", "help"], check=True)
