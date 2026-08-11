# Push current folder to the configured Git remote
# Usage:
#   .\push_python_repo.ps1 -CommitMessage "My update"
# Before using this, make sure you have set your remote to the GitHub repo:
#   git remote add origin https://github.com/<your-username>/python.git
#   git branch -M main
#   git push -u origin main

param(
    [string]$CommitMessage = "Update code"
)

git add .
$changes = git status --porcelain
if (-not $changes) {
    Write-Output "No changes to commit."
    exit 0
}

git commit -m $CommitMessage

git push origin main
