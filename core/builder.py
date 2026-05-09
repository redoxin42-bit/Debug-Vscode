from pathlib import Path
import subprocess

def build_apk(project_path: str):
    project = Path(project_path)

    if not project.exists():
        return False, f"Проект не найден: {project_path}"

    try:
        result = subprocess.run(
            ["buildozer", "-v", "android", "debug"],
            cwd=str(project),
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return True, result.stdout
        return False, result.stderr or result.stdout
    except Exception as e:
        return False, str(e)
