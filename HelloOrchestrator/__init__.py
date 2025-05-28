from azure.durable_functions import DurableOrchestrationContext, Orchestrator
import logging

def orchestrator_function(context: DurableOrchestrationContext):
    cep = context.get_input().get("cep")
    username = context.get_input().get("username")
    
    result1 = yield context.call_activity('ViaCep', cep)
    result2 = yield context.call_activity('Github', username)
    
    return [result1, result2]  # Retorna apenas o dicionário direto (opcionalmente poderia manter como lista)

main = Orchestrator.create(orchestrator_function)