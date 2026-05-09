from pathlib import Path

def read_file(file_path: str):
    path = Path(file_path)
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8", errors="ignore")

def write_file(file_path: str, content: str):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True
