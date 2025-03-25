import subprocess
from pathlib import Path
from argparse import ArgumentParser, Namespace
from a2s.commands import Command

class Container(Command):

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("robot", type=str.lower, choices=["base"])

    def execute(self, args: Namespace):

        if args.robot == "base":
            subprocess.run(["apptainer", "shell", "base.sif"], check=True, cwd=Path().home() / ".a2s")
