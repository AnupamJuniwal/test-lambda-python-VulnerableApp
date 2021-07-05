handler_name = 'file'

def handler(args):
    type, path = args
    switcher = {
        'read': file_read,
        'write': file_write
    }
    data = switcher[type](path, args)
    return data

def file_read(path, args):
    text = ""
    try:
        f = open(path, "r", encoding='utf-8')
        text = f.read()
    except:
        pass
    return text

def file_write(path, args):
    try:
        f = open(path, "a")
        f.write("Now the file has more content!\n")
    except:
        pass
    return 'done'
