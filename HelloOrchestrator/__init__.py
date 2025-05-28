from azure.durable_functions import DurableOrchestrationContext, Orchestrator
import logging

def orchestrator_function(context: DurableOrchestrationContext):
    """
    Orchestrator function that coordinates the execution of activities.
    It retrieves 'cep' and 'username' from the input, calls the ViaCep and Github activities,
    and returns their results.
    :param context: DurableOrchestrationContext object
    :return: List containing the results of the ViaCep and Github activities
    """
    logging.info('Starting orchestrator function.')
    if not context.get_input():
        raise ValueError("Input is required for the orchestrator function.")
    if not isinstance(context.get_input(), dict):
        raise TypeError("Input must be a dictionary containing 'cep' and 'username'.")
    
    cep = context.get_input().get("cep")
    if not cep or not isinstance(cep, str):
        raise ValueError("'cep' is required and must be a string.")
    
    username = context.get_input().get("username")
    if not username or not isinstance(username, str):
        raise ValueError("'username' is required and must be a string.")
    
    logging.info(f"Received cep: {cep}, username: {username}")
    
    # Chama as atividades ViaCep e Github
    result1 = yield context.call_activity('ViaCep', cep)
    result2 = yield context.call_activity('Github', username)
    logging.info(f"ViaCep result: {result1}, Github result: {result2}")
    # Retorna os resultados como uma lista de dicionários
    return [result1, result2]  # Retorna apenas o dicionário direto (opcionalmente poderia manter como lista)

main = Orchestrator.create(orchestrator_function)