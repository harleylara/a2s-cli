import argparse
from a2s.commands import Command, Run

COMMAND_OPTS: dict[str, type[Command]] = {
    "run": Run
}

def main(args=None) -> None:

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
