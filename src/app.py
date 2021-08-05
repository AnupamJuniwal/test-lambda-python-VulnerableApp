import json
import os
from src.controllers import handler_dict
# import requests



def lambda_handler(event, context):
    strBody = event.get('body')
    headers = event.get('headers')
    jsonBody = json.loads(strBody)
    if strBody is None or jsonBody is None or jsonBody.get('runner') is None:
            raise Exception('Please specify a runner')

    if headers is None or (headers.get('Content-Type') != 'application/json' and headers.get('content-type')  != 'application/json'):
            raise Exception('Unknown Content type')
    try:
        result = handler_dic[jsonBody.get('runner')](jsonBody.get('args'))
        if type(result) == type({}):
            result = json.dump(result)
        return {
            "statusCode": 200,
            "body": result,
        }
    except Exception as e:
        return {
            "statusCode": 501,
            "body": e.__cause__,
        }
