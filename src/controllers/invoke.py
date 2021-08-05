import boto3

client = boto3.client('lambda')

handler_name = 'invokeLambda'

def handler(args):
    arn, version, data = args
    print('invoking lambda arn: {}'.format(arn))
    print('invoking lambda version: {}'.format(version))
    print('invoking lambda data: {}'.format(data))
    response = client.invoke(
        FunctionName = arn,
        InvocationType ='Event',
        LogType ='Tail',
        ClientContext = '{}',
        Payload = bytes(data, 'utf-8'),
        Qualifier = version
    )
    print('invoking lambda invokeResult: {}'.format(response))
    return response