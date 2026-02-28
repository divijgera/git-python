class FileUtils:
    @staticmethod
    def read_file_bytes(path: str) -> bytes:
        try:
            with open(path, "rb") as f:
                return f.read()
        except FileNotFoundError:
            raise ValueError(f"Object not found at path {path}")