import subprocess
import sys
from pathlib import Path


def run_git(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        sys.exit(result.returncode)
    return result.stdout.strip()


def main():
    repo = Path.cwd()
    if not (repo / ".git").exists():
        run_git("init")
        run_git("branch", "-M", "main")
        run_git("remote", "add", "origin", "https://github.com/sreenandhan-17/python-.git")

    status = run_git("status", "--porcelain")
    if not status:
        print("No changes to commit.")
        return

    commit_message = " ".join(sys.argv[1:]) or "Update code"
    run_git("add", ".")
    run_git("commit", "-m", commit_message)
    run_git("push", "origin", "main")
    print("Pushed to origin/main.")


if __name__ == "__main__":
    main()
