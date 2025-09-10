import requests
import json

def fetch_github_repos(user="octocat"):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    repos = fetch_github_repos()
    with open("repos.json", "w") as f:
        json.dump(repos, f, indent=2)
    print("Saved repos.json")
