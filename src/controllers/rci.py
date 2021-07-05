
handler_name = 'rci'

def handler(args):
    script, = args
    data = rci_eval(script)
    return data


def rci_eval(script):
    text = eval(script)
    return text