from pathlib import Path

# get the name of the package
# and create a path to ~/.<package-name>
WORK_DIR = Path().home() / f".{__package__}"
CONTAINERS_DIR = WORK_DIR / "containers" # from setup.py

# base: it is not a robot by itself but is the base config
# for all the robots
SUPPORTED_ROBOTS = ["base", "foxy"]
