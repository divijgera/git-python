from app.commands import CommandFactory
from app.utils import GitParser

def main():
    parser = GitParser.get_git_parser()
    args = parser.parse_args()
    command = args.command

    git_command = CommandFactory.get_command(command)

    if command == "init":
        git_command.process()
    elif command == "cat-file":
        git_command.process(mode=args.mode, object=args.object)
    elif command == "hash-object":
        git_command.process(mode=args.mode, file=args.file)
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
