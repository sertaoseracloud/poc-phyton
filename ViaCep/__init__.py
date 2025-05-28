import requests
import logging

def main(cep: str) -> dict:
    """
    Consulta informações de endereço a partir de um CEP usando a API ViaCEP.
    :param cep: Código de Endereçamento Postal (CEP) a ser consultado
    :return: Dicionário com os dados do endereço
    """
    if not cep or not isinstance(cep, str):
        raise ValueError("O parâmetro 'cep' é obrigatório e deve ser uma string.")
    if not cep.isdigit() or len(cep) != 8:
        raise ValueError("O parâmetro 'cep' deve conter exatamente 8 dígitos numéricos.")
    logging.info(f"Consultando o CEP: {cep}")
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
