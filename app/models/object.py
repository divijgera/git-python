from dataclasses import dataclass

@dataclass
class GitObject:
    type: str
    content: bytes
    size: int