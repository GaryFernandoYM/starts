import os

def list_files(directory: str) -> list[str]:
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
