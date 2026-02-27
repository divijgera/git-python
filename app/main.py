from argparse import ArgumentParser
import argparse
from app.commands import init, cat_file

def generate_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(description="A simple implementation of git in Python")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init", help="Initialize a new git repository")

    cat_parser = subparsers.add_parser("cat-file", help="Provide content or type and size information for repository objects")
    mode = cat_parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("-p", dest="mode", action="store_const", const="pretty", help="Pretty-print the contents of the object based on its type")
    mode.add_argument("-t", dest="mode", action="store_const", const="type", help="Show the type of the object")
    mode.add_argument("-s", dest="mode", action="store_const", const="size", help="Show the size of the object")
    cat_parser.add_argument("object", help="The object SHA-1")

    return parser

def main():
    parser = generate_parser()
    args = parser.parse_args()
    command = args.command

    if command == "init":
        init.main()
    elif command == "cat-file":
        cat_file.main(args.mode, args.object)
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
