from pathlib import Path
import subprocess
from argparse import ArgumentParser, Namespace
from a2s.commands import Command

class Update(Command):

    def add_arguments(self, parser: ArgumentParser):
        pass

    def execute(self, args: Namespace):
        subprocess.run(["bash", "install.sh", "update"], check=True, cwd=Path().home() / "a2s-cli")
        return
