from app.utils import FileUtils, GitUtils
from .git_command import GitCommand

class CatFile(GitCommand):
    def validate_args(self, **kwargs):
        object_sha = kwargs["object"]

        if "mode" not in kwargs or kwargs["mode"] not in ["pretty", "type", "size"]:
            raise ValueError(f"Invalid mode {kwargs["mode"]} for cat-file command")
        
        if len(object_sha) != 40:
            raise ValueError(f"Object SHA-1 should be 40 characters long, got {len(object_sha)}")

    def process(self, **kwargs):
        self.validate_args(**kwargs)

        mode = kwargs["mode"]
        object_sha = kwargs["object"]   

        dir_name = object_sha[:2]
        file_name = object_sha[2:]
        object_path = f".git/objects/{dir_name}/{file_name}"
        raw_data = FileUtils.read_file_bytes(object_path)
        git_object = GitUtils.decompress_and_get_git_object_content(raw_data)

        if mode == "pretty":
            print(git_object.content.decode("utf-8"), end="")
        elif mode == "type":
            print(git_object.type, end="")
        elif mode == "size":
            print(git_object.size, end="")
        else:
            raise NotImplementedError(f"Mode {mode} not implemented yet")

