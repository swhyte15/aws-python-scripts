import boto3
import json

def invoke_lambda(function_name, payload):
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )
    return json.load(response['Payload'])
