import argparse
import subprocess
from pathlib import Path
from argparse import ArgumentParser, Namespace
from a2s.commands import Command

class Run(Command):

    def add_arguments(self, parser: ArgumentParser):
        """

        Arguments:
        - `--raw`: if this parameter is passed, all other parameters are ignored
            and everything after it is passed directly
            to the internal command. Equivalently to `a2s run --raw <opts...>` -> `apptainer run <opts...>`.
            Important: the underlying command is executed in the `~/.a2s` folder by default.
        """
        parser.add_argument("robot", type=str.lower, choices=["base"])
        parser.add_argument("--path", type=str.lower, default=Path().home() / ".a2s", choices=["base"], help="Path from where to run this command.")
        parser.add_argument("--raw", nargs=argparse.REMAINDER, help="Pass raw arguments to underlying apptainer")

    def execute(self, args: Namespace):

        if args.raw:
            full_cmd = ["apptainer", "run"] + args.raw
            subprocess.run(full_cmd, check=True, cwd=Path().home() / ".a2s")
            return


        # if args.robot == "base":
        #     # subprocess.run(["apptainer", "run", "--bind", "/run/user:/run/user", "base.sif"], check=True, cwd=Path().home() / ".a2s")
        #     subprocess.run(["apptainer", "run", "base.sif"], check=True, cwd=Path().home() / ".a2s")
