import requests
import http.client

handler_name = 'ssrf'

def handler(args):
    type, url = args
    switcher = {
        'requests': ssrf_get,
        'http': ssrf_httpclient
    }
    data = switcher[type](url, args)
    return data

def ssrf_get(url, _args):
    r = requests.get("http://{url}".format(url=url))
    return r.text


def ssrf_httpclient(url, _args):
    connection = http.client.HTTPConnection(url)
    connection.request("GET", "/")
    response = connection.getresponse().read()
    return response