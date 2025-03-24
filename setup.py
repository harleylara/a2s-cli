from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

def boostrap_install():
    pass


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
