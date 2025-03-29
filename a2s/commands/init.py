import subprocess
from argparse import ArgumentParser, Namespace
from a2s.commands import Command
from a2s.config import CONTAINERS_DIR, SUPPORTED_ROBOTS, WORK_DIR, DEFITIONS_DIR

class Init(Command):
    """
    Creates the desired robot container.

    format:
        a2s init <robot>
    """

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("robot", type=str.lower, choices=SUPPORTED_ROBOTS, help="robot container to initialize.")

    def execute(self, args: Namespace):

        WORK_DIR.mkdir(exist_ok=True)
        DEFITIONS_DIR.mkdir(exist_ok=True)
        CONTAINERS_DIR.mkdir(exist_ok=True)

        # check for base and make sure exists
        if not (CONTAINERS_DIR / "base.sif").exists():
            print("Base container not found")
            print("Building base first")
            subprocess.run(
                [
                    "apptainer",
                    "build",
                    "--force",
                    CONTAINERS_DIR / "base.sif",
                    DEFITIONS_DIR / "base.def",
                ],
                cwd=WORK_DIR,
                check=True
            )

        cmd_run = ["apptainer", "build", f"{args.robot}.sif", DEFITIONS_DIR / f"{args.robot}.def"]

        subprocess.run(cmd_run, cwd=CONTAINERS_DIR, check=True)
