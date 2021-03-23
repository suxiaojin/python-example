'''
isinstance() --判断一个对象是某个子类或子类的实例.检测是不是摸个类型。
a=5
isinstance(a,int)
'''

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