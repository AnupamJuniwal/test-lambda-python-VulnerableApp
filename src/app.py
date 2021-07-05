import json
import ptvsd
from src.controllers import handler_dic
# import requests


ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
ptvsd.wait_for_attach()

def lambda_handler(event, context):
    ptvsd.break_into_debugger()

    if event.body == None or event.body.runner == None:
            raise Exception('Please specify a runner')
    
    if event.headers == None or (event.headers['Content-Type'] != 'application/json' and event.headers['content-type']  != 'application/json'): 
            raise Exception('Unknown Content type')
    try:
        result = handler_dic[event.body.runner](event.body.args)
    except Exception as e:
        result = e.__cause__
    if type(result) == type({}):
        result = json.dump(result)

    return {
        "statusCode": 200,
        "body": result,
    }
