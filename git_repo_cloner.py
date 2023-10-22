import subprocess

def clone_repositories(repo_list):
    for repo in repo_list:
        subprocess.run(["git", "clone", repo])

repositories = [
    "https://github.com/example/repo1.git",
    "https://github.com/example/repo2.git",
    # Add more repositories as needed
]

clone_repositories(repositories)
