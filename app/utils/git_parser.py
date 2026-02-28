from argparse import ArgumentParser
import argparse

class GitParser:

    @staticmethod
    def get_git_parser() -> ArgumentParser:
        parser = argparse.ArgumentParser(description="A simple implementation of git in Python")
        subparsers = parser.add_subparsers(dest="command", required=True)

        subparsers.add_parser("init", help="Initialize a new git repository")

        cat_parser = subparsers.add_parser("cat-file", help="Provide content or type and size information for repository objects")
        mode = cat_parser.add_mutually_exclusive_group(required=True)
        mode.add_argument("-p", dest="mode", action="store_const", const="pretty", help="Pretty-print the contents of the object based on its type")
        mode.add_argument("-t", dest="mode", action="store_const", const="type", help="Show the type of the object")
        mode.add_argument("-s", dest="mode", action="store_const", const="size", help="Show the size of the object")
        cat_parser.add_argument("object", help="The object SHA-1")

        hash_object_parser = subparsers.add_parser("hash-object", help="Compute object ID and optionally creates a blob from a file")
        mode = hash_object_parser.add_mutually_exclusive_group(required=True)
        mode.add_argument("-w", dest="mode", action="store_const", const="write", help="Actually write the object into the object database")
        hash_object_parser.add_argument("file", help="The file to hash")

        return parser
