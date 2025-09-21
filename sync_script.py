import os
import shutil
import subprocess
from pathlib import Path

# -------- CONFIG --------
TARGET_DIR = r"C:\Users\Lenovo\Desktop\New folder\Target"  # Change this to your target directory
SCRIPT_NAME = "sync_script.py"  # Name of this script
BRANCH = "main"
# ------------------------

ROOT_DIR = Path(__file__).parent

def run_git_commands(message):
    """Run git add, commit, and push with a given commit message."""
    subprocess.run(["git", "add", "."], cwd=ROOT_DIR)
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT_DIR)
    subprocess.run(["git", "push", "origin", BRANCH], cwd=ROOT_DIR)

def clean_root():
    """Delete all files/folders in root except .git and this script."""
    for item in ROOT_DIR.iterdir():
        if item.name in [".git", SCRIPT_NAME]:
            continue
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

def copy_from_target():
    """Copy all files/folders from target directory into root."""
    for item in Path(TARGET_DIR).iterdir():
        dest = ROOT_DIR / item.name
        if item.is_file():
            shutil.copy(item, dest)
        elif item.is_dir():
            shutil.copytree(item, dest)

def main():
    # Check if files (other than .git and script) exist
    files_in_root = [f for f in ROOT_DIR.iterdir() if f.name not in [".git", SCRIPT_NAME]]

    if files_in_root:  
        print("Files found in root, cleaning...")
        clean_root()
        run_git_commands("Cleaned files from root directory")
    else:
        print("No files in root, copying from target...")
        copy_from_target()
        run_git_commands("Copied files from target directory")

if __name__ == "__main__":
    main()