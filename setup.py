import sys
import shutil
import subprocess
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

__package__ = "a2s"

def boostrap_install():

    host_platform = sys.platform

    if not host_platform.startswith("linux"):
        sys.stderr.write(f"Platform {host_platform} not supported. Only linux systems.")
        sys.exit(1)

    if shutil.which("apptainer") is None:
        sys.stderr.write(f"\nError: 'apptainer' is not installed.\n")
        sys.exit(1)

    work_dir = Path().home() / f".{__package__}"
    definitions_dir = work_dir / "definitions"
    definitions_dir.mkdir(exist_ok=True, parents=True)

    shutil.copytree("./definitions/", definitions_dir, dirs_exist_ok=True)
    shutil.copy("./install.sh", work_dir, dirs_exist_ok=True)


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
