import requests
import logging

def main(cep: str) -> dict:
    """
    Retrieves address information from a CEP (Brazilian postal code) using the ViaCEP API.
    :param cep: Postal code (CEP) to be queried
    :return: Dictionary with address data
    """
    if not cep or not isinstance(cep, str):
        raise ValueError("The 'cep' parameter is required and must be a string.")
    if not cep.isdigit() or len(cep) != 8:
        raise ValueError("The 'cep' parameter must contain exactly 8 numeric digits.")
    logging.info(f"Querying CEP: {cep}")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get('erro'):
            raise ValueError(f"CEP {cep} not found.")
        return data
    except requests.RequestException as e:
        logging.error(f"Error querying CEP {cep}: {e}")
        raise
