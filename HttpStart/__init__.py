import logging

from azure.functions import HttpRequest, HttpResponse
from azure.durable_functions import DurableOrchestrationClient

async def main(req: HttpRequest, starter: str) -> HttpResponse:
    client = DurableOrchestrationClient(starter)
    function_name = req.route_params.get("functionName")

    if not function_name:
        return HttpResponse("Function name is required in the route.", status_code=400)

    data = req.get_json()
    cep = data.get('cep')
    username = data.get('username')
    if not cep or not username:
        return HttpResponse("Both 'cep' and 'username' are required in the request body.", status_code=400)
    if not isinstance(cep, str) or not isinstance(username, str):
        return HttpResponse("'cep' and 'username' must be strings.", status_code=400)
    
    instance_id = await client.start_new(function_name, None, {
        'cep': cep,
        'username': username
    })
    
    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    return client.create_check_status_response(req, instance_id)
