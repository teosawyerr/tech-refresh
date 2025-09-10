from python_scripts.api_fetch import fetch_github_repos

def test_fetch_github_repos():
    repos = fetch_github_repos("octocat")
    assert isinstance(repos, list)
    assert "id" in repos[0]
