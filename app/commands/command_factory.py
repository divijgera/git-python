

from app.commands.git_command import GitCommand
from app.commands.init import Init
from app.commands.cat_file import CatFile
from app.commands.hash_object import HashObject

class CommandFactory:
    @staticmethod
    def get_command(command_name: str) -> GitCommand:
        if command_name == "init":
            return Init()
        elif command_name == "cat-file":
            return CatFile()
        elif command_name == "hash-object":
            return HashObject()
        else:
            raise ValueError(f"Unknown command {command_name}")