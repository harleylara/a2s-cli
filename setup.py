import sys
import shutil
import subprocess
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

__package__ = "a2s"
WORK_DIR = Path().home() / f".{__package__}"
DEFITIONS_DIR = WORK_DIR / "definitions"
CONTAINERS_DIR = WORK_DIR / "containers"

def boostrap_install():

    host_platform = sys.platform

    if not host_platform.startswith("linux"):
        sys.stderr.write(f"Platform {host_platform} not supported. Only linux systems.")
        sys.exit(1)

    if shutil.which("apptainer") is None:
        sys.stderr.write(f"\nError: 'apptainer' is not installed.\n")
        sys.exit(1)

    WORK_DIR.mkdir(exist_ok=True)

    DEFITIONS_DIR.mkdir(exist_ok=True)
    CONTAINERS_DIR.mkdir(exist_ok=True)

    shutil.copytree("./definitions/", DEFITIONS_DIR, dirs_exist_ok=True)

    # always build base.def first
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

    for item in DEFITIONS_DIR.iterdir():
        # skip base.def
        if item.is_file() and (item.stem != "base"):
            subprocess.run(["apptainer", "build", f"{item.stem}.sif", DEFITIONS_DIR / item.name], cwd=CONTAINERS_DIR, check=True)


class DevelopCmd(develop):

    def run(self) -> None:
        boostrap_install()
        super().run()


class InstallCmd(install):

    def run(self) -> None:
        boostrap_install()
        super().run()


setup(
    name=__package__,
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
    ],
    cmdclass={
        "install": InstallCmd,
        "develop": DevelopCmd
    },
    entry_points={
        "console_scripts": [
            "a2s = a2s.main:main"
        ]
    },
    python_requires=">=3.9"
)
