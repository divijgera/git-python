from .git_command import GitCommand
from app.utils import FileUtils, GitUtils

class HashObject(GitCommand):
    def validate_args(self, **kwargs):
        if "mode" not in kwargs or kwargs["mode"] not in ["write"]:
            raise ValueError("hash-object received an invalid mode argument")
        
        if "type" in kwargs and kwargs["type"] not in ["blob", "tree", "commit"]:
            raise ValueError("hash-object received an invalid type argument")
        
        if "file" not in kwargs:
            raise ValueError("hash-object command requires a file argument")
    
    def process(self, **kwargs):
        self.validate_args(**kwargs)
        file = kwargs["file"]

        file_bytes = FileUtils.read_file_bytes(file)
        object_type = kwargs.get("type", "blob")
        git_object = GitUtils.generate_git_object_from_file_bytes(file_bytes, object_type)
        sha1 = GitUtils.hash_git_object(git_object)
        print(sha1, end="")

        if "mode" in kwargs and kwargs["mode"] == "write":
            GitUtils.write_git_object(git_object)