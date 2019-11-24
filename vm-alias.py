#!/usr/bin/env python
import subprocess
import sys

def start(vm_name,is_headless):
    cmd = ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe","startvm",vm_name] 
    if is_headless:
        cmd.append('--type')
        cmd.append('headless')
    return cmd

def close(vm_name):
    return ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe","controlvm",vm_name,"acpipowerbutton"]

def wrapBrackets(lst):
    reserved = ['False','True']
    for i in range(len(lst)):
        if not lst[i] in reserved:
            lst[i] = '"'+ lst[i] +'"'
    return lst 

if __name__ == "__main__":
    call = sys.argv[1]
    args = ','.join(wrapBrackets(sys.argv[2:]))
    # print("{}({})".format(call,args))  #Debug
    cmd = eval("{}({})".format(call,args))
    print(subprocess.list2cmdline(cmd))
    subprocess.call(cmd)