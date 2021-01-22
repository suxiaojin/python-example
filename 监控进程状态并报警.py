#1.检测进程存在
import psutil
def checkprocess(pname):
    pl=psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name()=pname:
            return pid

if isinstance(checkprocess('java'),int):
    print('进程存在')

else:
    print('进程不存在')

