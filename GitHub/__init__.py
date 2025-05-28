import requests

def main(username: str) -> dict:
    """
    Consulta informações públicas de um usuário do GitHub.
    :param username: Nome de usuário no GitHub
    :return: Dicionário com os dados do usuário
    """
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Erro ao consultar o usuário {username} no GitHub: {e}")
