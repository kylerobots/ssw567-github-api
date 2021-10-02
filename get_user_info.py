import requests
from typing import Dict


def getUserInfo(username: str) -> Dict[str, int]:
    """!
    @brief Returns the repositories and number of commits for a given username on GitHub

    @param username The username to lookup on GitHub
    @return Dict[str, int] A dictionary where the keys are the names of public repositories and values are the number
    of commits per repository.
    @raises TypeError Thrown if the provided input cannot resolve to a string in the URL.
    """
    # Ensure the input is actually a string.
    if not isinstance(username, str):
        raise TypeError('Username must be a String object')
    # Create the URL to look up repositories.
    user_url = 'https://api.github.com/users/{0:s}/repos'.format(username)
    # Get the list of repositories. I had to look this up from https://docs.python-requests.org/en/latest/ as I have
    # never dealt with this library before.
    user_result = requests.get(user_url)
    response = dict()
    # The status code tells if the lookup was successful or not
    if user_result.status_code == 200:
        # The top level elements in the object are the repositories. So iterate through those to look up the number of
        # commits.
        for repo in user_result.json():
            repo_name = repo['name']  # type: ignore
            repo_url = 'https://api.github.com/repos/{0:s}/{1:s}/commits'.format(
                username, repo_name)
            repo_result = requests.get(repo_url).json()
            # The top level elements of this response are the individual commits. Count them.
            commit_count = len(repo_result)
            response[repo_name] = commit_count
    return response
