import os
import subprocess

handler_name = 'rce'

def handler(args):
    type, cmd = args
    switcher = {
        'os': rce_os,
        'subprocess': rce_subprocess
    }
    data = switcher[type](cmd, args)
    return data


def rce_os(command, _args):
    output = os.system(command)
    print("os.system output : {}".format(output))
    stream = os.popen(command)
    stream_output = stream.read()
    print("os.popen output : {}".format(stream_output))
    output = str(output) + stream_output
    return output

def rce_subprocess(command, _args):
    # thread.start_new_thread(foo, ("Thread-1", command ));
    output = subprocess.run([command])
    print("subprocess.run output : {}".format(output))
    output = subprocess.check_output([command])
    print("subprocess.check_output output : {}".format(output))
    output = subprocess.Popen(command, stdout=subprocess.PIPE)
    print("subprocess.Popen output : {}".format(output))
    output = subprocess.call(command, shell=True)
    print("subprocess.call output : {}".format(output))
    return "RCE through subprocess done"