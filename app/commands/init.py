import os
from .git_command import GitCommand

class Init(GitCommand):
    def validate_args(self, **kwargs):
        if len(kwargs) != 0:
            raise ValueError("init command does not take any arguments")

    def process(self, **kwargs):
        self.validate_args(**kwargs)

        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")

        print("Initialized git directory")