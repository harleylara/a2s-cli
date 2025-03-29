from pathlib import Path

WORK_DIR = Path().home() / f".{__package__}"

CONTAINERS_DIR = WORK_DIR / "containers"
DEFITIONS_DIR = WORK_DIR / "definitions"

SUPPORTED_ROBOTS = ["base", "foxy"]
