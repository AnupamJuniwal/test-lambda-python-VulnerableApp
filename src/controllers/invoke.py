import boto3
import traceback

client = boto3.client('lambda')

handler_name = 'invokeLambda'

def handler(args):
    arn, version, data = args
    response = None
    try:
        response = client.invoke(
            FunctionName = arn,
            InvocationType ='Event',
            LogType ='Tail',
            # ClientContext = '{}',
            Payload = bytes(data, 'utf-8'),
            Qualifier = version
        )["ResponseMetadata"]
    except Exception as e: 
        print("Error while invoking another lambda:", e.__cause__)
        traceback.print_tb(e.__traceback__)
    print('invoking lambda invokeResult: {}'.format(response))
    return response