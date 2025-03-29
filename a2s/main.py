import argparse
from a2s.commands import Command, Run, Init, Update

"""
All commands exposed in this tool must be explicitly
registered in this dictionary (`COMMAND_OPTS`), where the key 
is the name of the command exposed to the user and
the value is the implementation of the command.
"""
COMMAND_OPTS: dict[str, type[Command]] = {
    "run": Run,
    "init": Init,
    "update": Update
}

def main(args=None) -> None:
    """
    This is the main entry point for this cli tool.

    The main purpose of this section is to dispatch the commands. All commands
    follow the form:

        a2s <command REQUIRED> <args...>

    All commands must be derived from the base class `Command`.
    """

    parser = argparse.ArgumentParser(
        prog="a2s",
        description="a2s cli tool for managing a2s robots"
    )

    subparsers = parser.add_subparsers(dest="command",
                                       required=True,
                                       help="Execution command")

    for cmd_name, cmd_cls in COMMAND_OPTS.items():
        subparser = subparsers.add_parser(cmd_name, help=f"{cmd_name} command")
        cmd_cls().add_arguments(subparser)

    args = parser.parse_args()
    cmd_cls = COMMAND_OPTS[args.command]

    if cmd_cls:
        cmd_cls().execute(args)
    else:
        parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
