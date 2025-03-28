import argparse
import subprocess
from argparse import ArgumentParser, Namespace
from a2s.commands import Command
from a2s.config import CONTAINERS_DIR, SUPPORTED_ROBOTS

class Run(Command):

    def add_arguments(self, parser: ArgumentParser):
        """

        Arguments:
        """
        parser.add_argument("robot", type=str.lower, choices=SUPPORTED_ROBOTS)
        parser.add_argument("--path", type=str.lower, default=CONTAINERS_DIR, help="Path from where to run this command.")
        parser.add_argument(
            "--raw",
            nargs=argparse.REMAINDER, 
            help="""
if this parameter is passed, all other parameters are ignored
and everything after it is passed directly
to the internal command. Equivalently to `a2s run --raw <opts...>` -> `apptainer run <opts...>`.
Important: the underlying command is executed in the `~/.a2s` folder by default."""
        )

    def execute(self, args: Namespace):

        if args.raw:
            full_cmd = ["apptainer", "run"] + args.raw
            subprocess.run(full_cmd, check=True, cwd=args.path)
            return

        # TODO: FIX change shell for RUN but add a startscript
        run_cmd = ["apptainer", "shell", f"{args.robot}.sif"]
        subprocess.run(run_cmd, check=True, cwd=args.path)

