import sys
import shutil
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

def boostrap_install():

    host_platform = sys.platform

    if not host_platform.startswith("linux"):
        sys.stderr.write(f"Platform {host_platform} not supported. Only linux systems.")
        sys.exit(1)

    if shutil.which("apptainer") is None:
        sys.stderr.write(f"\nError: 'apptainer' is not installed.\n")
        sys.exit(1)

    WORK_DIR = Path().home() / f".a2s"
    WORK_DIR.mkdir(exist_ok=True)

    if host_platform.startswith("darwin"):
        # MacOs Install
        pass

    # sudo apt install apptainer


class DevelopCmd(develop):

    def run(self) -> None:
        boostrap_install()
        super().run()


class InstallCmd(install):

    def run(self) -> None:
        boostrap_install()
        super().run()


setup(
    name='a2s',
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
