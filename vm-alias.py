#!/usr/bin/env python
import subprocess
import sys
import psutil


def start(vm_name, is_headless=True):
    cmd = ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", "startvm", vm_name]
    if is_headless:
        cmd.append('--type')
        cmd.append('headless')
    return cmd


def close(vm_name):
    return ["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", "controlvm", vm_name, "acpipowerbutton"]


def listall():
    # FIXME
    procs = {p.pid: p for p in psutil.process_iter(
    ) if "VirtualBoxVM.exe" == p.name() or "VBoxHeadless.exe" == p.name()}
    machines = {procs[m].cmdline()[2]: 1 for m in procs}
    print(machines)


def wrapBrackets(lst):
    reserved = ['False', 'True']
    for i in range(len(lst)):
        if not lst[i] in reserved:
            lst[i] = '"' + lst[i] + '"'
    return lst


if __name__ == "__main__":
    # functions that should now run in command line
    exclude = ['listall']
    call = sys.argv[1]
    args = ','.join(wrapBrackets(sys.argv[2:]))
    # print("{}({})".format(call, args))  # Debug
    cmd = eval("{}({})".format(call, args))
    if not call in exclude:
        print(subprocess.list2cmdline(cmd))
        subprocess.call(cmd)
