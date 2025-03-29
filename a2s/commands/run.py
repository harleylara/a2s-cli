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

        if not (CONTAINERS_DIR / f"{args.robot}.sif").exists():
            print(f"The '{args.robot}' robot container has not been found.\n")
            print("be sure to initialize the container (one-time operation)")
            print("use the command:\n\n")
            print(f"    a2s init {args.robot}\n\n")
            print("this operation may take time")
            return

        if args.raw:
            full_cmd = ["apptainer", "run"] + args.raw
            subprocess.run(full_cmd, check=True, cwd=args.path)
            return

        run_cmd = ["apptainer", "run", f"{args.robot}.sif"]
        subprocess.run(run_cmd, check=True, cwd=args.path)

