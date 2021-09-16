import json
import os
import traceback
import base64

from src.controllers import handler_dict
# import requests



def lambda_handler(event, context):
    strBody = event.get('body')
    print("Got body: {}".format(strBody))
    headers = event.get('headers')
    if headers is None or (headers.get('Content-Type') != 'application/json' and headers.get('content-type')  != 'application/json'):
            raise Exception('Unknown Content type')

    isBase64Encoded = event.get('isBase64Encoded')
    if isBase64Encoded is True: 
        strBody = base64.b64decode(strBody).decode("utf-8")
    jsonBody = json.loads(strBody)
    
    if strBody is None or jsonBody is None or jsonBody.get('runner') is None:
            raise Exception('Please specify a runner')
    try:
        result = handler_dict[jsonBody.get('runner')](jsonBody.get('args'))
        result = result or ""
        if type(result) is type({}):
            result = json.dumps(result)
        return {
            "statusCode": 200,
            "body": result,
        }
    except Exception as e:
        print("Exception in app: {}".format(e.__class__))
        traceback.print_tb(e.__traceback__)
        return {
            "statusCode": 501,
            "body": e.__cause__,
        }
