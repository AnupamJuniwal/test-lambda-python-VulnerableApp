import time

handler_name = 'lateReply'

def handler(args):
    t, = args
    try:
        time.sleep(t/1000)
        return 'done'
    except Exception as e: 
        return 'failed'