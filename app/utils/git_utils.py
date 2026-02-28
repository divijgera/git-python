from app.models import GitObject
import hashlib
import os
import zlib

class GitUtils:
    @staticmethod
    def get_git_object(git_data: bytes) -> GitObject:
        headers, content = git_data.split(b"\x00", 1)

        type_str, size_str = headers.split(b" ", 1)
        size = int(size_str)
        if size != len(content):
            raise ValueError(f"Expected size {size} does not match actual content size {len(content)}")
        
        return GitObject(
            type=type_str.decode("utf-8"),
            content=content,
            size=size,
        )
    
    @staticmethod
    def decompress_and_get_git_object_content(compressed_data: bytes) -> GitObject:
        decompressed_data = zlib.decompress(compressed_data)
        git_object = GitUtils.get_git_object(decompressed_data)
        return git_object
    
    @staticmethod
    def generate_git_object_from_file_bytes(file_bytes: bytes, object_type: str) -> GitObject:
        return GitObject(
            type=object_type,
            content=file_bytes,
            size=len(file_bytes),
        )
    
    @staticmethod
    def serialize_git_object(git_object: GitObject) -> bytes:
        header = f"{git_object.type} {git_object.size}\x00".encode("utf-8")
        return header + git_object.content

    @staticmethod
    def serialize_and_compress_git_object_as_content(git_object: GitObject) -> bytes:
        store_data = GitUtils.serialize_git_object(git_object)
        compressed_data = zlib.compress(store_data)
        return compressed_data
    
    @staticmethod
    def hash_git_object(git_object: GitObject) -> str:
        store_data = GitUtils.serialize_git_object(git_object)
        sha1 = hashlib.sha1(store_data).hexdigest()
        return sha1
    
    @staticmethod
    def hash_git_object_from_file_bytes(data: bytes, object_type: str) -> str:
        git_object = GitUtils.generate_git_object_from_file_bytes(data, object_type)
        return GitUtils.hash_git_object(git_object)
    
    @staticmethod
    def write_git_object(git_object: GitObject):
        sha1 = GitUtils.hash_git_object(git_object)
        dir_name = sha1[:2]
        file_name = sha1[2:]
        object_path = f".git/objects/{dir_name}/{file_name}"
        
        os.makedirs(f".git/objects/{dir_name}", exist_ok=True)

        compressed_data = GitUtils.serialize_and_compress_git_object_as_content(git_object)
        with open(object_path, "wb") as f:
            f.write(compressed_data)