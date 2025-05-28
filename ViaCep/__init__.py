import requests
import logging

def main(cep: str) -> dict:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get('erro'):
            raise ValueError(f"CEP {cep} não encontrado.")
        return data
    except requests.RequestException as e:
        logging.error(f"Erro ao consultar o CEP {cep}: {e}")
        raise
