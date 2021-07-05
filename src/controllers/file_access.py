import os

handler_name = 'path_traversal'

def handler(args):
    path, = args
    data = file_access_path_traversal(path)
    return data

def file_access_path_traversal(usrPath):
    print("Path traversal payload : {}".format(usrPath))
    path = os.getcwd() + "/" + usrPath
    print("path accessing: {}".format(path))
    data = open(path, "rb").read()
    print("path_traversal response : {}".format(data))
    return  data
