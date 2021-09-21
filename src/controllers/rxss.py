handler_name = 'rxss'

def handler(args):
    script, = args
    data = rxss_basic(script)
    return data

def rxss_basic(payload):
    print("rxss payload : {}".format(payload))
    html = "<!DOCTYPE html><html><head><title>XSS</title></head><body> Response here" + payload + "</body></html>"
    return html