import requests

def main(username: str) -> dict:
    """
    Retrieves public information about a GitHub user.
    :param username: GitHub username
    :return: Dictionary with user data
    """
    if not username or not isinstance(username, str):
        raise ValueError("The 'username' parameter is required and must be a string.")
    if not username.isalnum():
        raise ValueError("The 'username' parameter must contain only alphanumeric characters.")
    
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Error fetching user {username} from GitHub: {e}")
