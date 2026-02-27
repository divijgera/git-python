import zlib
from app.models import GitObject

def read_file_bytes(path: str) -> bytes:
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError(f"Object not found at path {path}")
    
def get_git_object(data: bytes) -> GitObject:
    headers, content = data.split(b"\x00", 1)

    type_str, size_str = headers.split(b" ", 1)
    size = int(size_str)
    if size != len(content):
        raise ValueError(f"Expected size {size} does not match actual content size {len(content)}")
    
    return GitObject(
        type=type_str.decode("utf-8"),
        content=content,
        size=size,
    )

def main(mode: str, object_sha: str):
    if len(object_sha) != 40:
        raise ValueError(f"Object SHA-1 should be 40 characters long, got {len(object_sha)}")
    
    dir_name = object_sha[:2]
    file_name = object_sha[2:]
    object_path = f".git/objects/{dir_name}/{file_name}"
    raw_data = read_file_bytes(object_path)
    decompressed_data = zlib.decompress(raw_data)

    git_object = get_git_object(decompressed_data)

    if mode == "pretty":
        print(git_object.content.decode("utf-8"), end="")
    elif mode == "type":
        print(git_object.type, end="")
    elif mode == "size":
        print(git_object.size, end="")
    else:
        raise NotImplementedError(f"Mode {mode} not implemented yet")
