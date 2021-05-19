import telnetlib
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from s_mail import SendEMail
import time

def get_ip_status(times,ip,port):
    server=telnetlib.Telnet()
    try:
        server.open(ip,port)
        print('time:{0} {1} port {2} is open'.format(times,ip,port))
    except Exception as err:
        print('******************************')
        print('time:{0} {1} node port {2} is not open'.format(times,ip, port))
        sm = SendEMail()
        sm.sendmail(['suxiaojin928380@126.com','49573261@qq.com','wangxiwei1012@163.com'], '轻钱包端口不通', '时间:%s ip:%s node端口:%s访问不通' %(times,ip,port))
    finally:
        server.close()


def check_port():
    f = open('list.txt', 'r')
    c = f.readlines()
    hosts= []
    threads = []
    times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    for n in c:
        n = n.strip('\n')
        hosts.append(n)
    for k in list(set(hosts)):
        for port in range(23454,23456):
            t=threading.Thread(target=get_ip_status,args=(times,k,port))
            t.start()
            threads.append(t)
    for t in threads:
            t.join()

def dojob():
    scheduler=BlockingScheduler()
    scheduler.add_job(check_port, 'interval',minutes=20,id='check_port')
    scheduler.start()

if __name__ == '__main__':
    dojob()

-----------------------------------------------------------------------------------------------------------------------------------
import telnetlib
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from s_mail import SendEMail

def get_ip_status(times,ip,port):
    server=telnetlib.Telnet()
    try:
        server.open(ip,port)
        print('time:{0} {1} port {2} is open'.format(times, ip, port))
    except Exception as err:
        print('time:{0} {1} node port {2} is not open'.format(times,ip, port))
        sm = SendEMail()
        sm.sendmail(['suxiaojin928380@126.com'], '轻钱包端口不通',
                    '时间:%s ip:%s node端口:%s访问不通' % (times, ip, port))
    finally:
        server.close()


def check_port():
    host='192.168.110.13'
    ports=[33033,3306,8440,80,5555,7777]
    times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    for port in ports:
        get_ip_status(times,host,port)



def dojob():
    scheduler=BlockingScheduler()
    scheduler.add_job(check_port, 'interval',minutes=1,id='check_port')
    scheduler.start()


if __name__ == '__main__':
    dojob()