import logging

from azure.functions import HttpRequest, HttpResponse
from azure.durable_functions import DurableOrchestrationClient

async def main(req: HttpRequest, starter: str) -> HttpResponse:
    """
    HTTP trigger function to start a Durable Function orchestration.
    This function expects a JSON body with 'cep' and 'username' fields,
    and a route parameter 'functionName' that specifies the orchestration function to start.
    :param req: HTTP request object
    :param starter: Connection string to the Durable Functions backend
    :return: HTTP response with the status of the orchestration
    """
    logging.info('Python HTTP trigger function processed a request.')
    if not starter:
        return HttpResponse("Durable Functions starter is not configured.", status_code=500)
    if not req.route_params:
        return HttpResponse("Function name is required in the route.", status_code=400)
    if not req.get_json:
        return HttpResponse("Request body must be JSON.", status_code=400)
    
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
