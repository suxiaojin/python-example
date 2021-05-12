import telnetlib
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from s_mail import SendEMail


def get_ip_status(ip,port):
    server=telnetlib.Telnet()
    try:
        server.open(ip,port)
        print('{0} port {1} is open'.format(ip,port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
        sm = SendEMail()
        sm.sendmail(['suxiaojin928380@126.com','49573261@qq.com','wangxiwei1012@163.com'], '轻钱包端口不通', 'ip%s端口%s访问不通' %(ip,port))
    finally:
        server.close()


def check_port():
    f = open('list.txt', 'r')
    c = f.readlines()
    hosts= []
    threads = []
    for n in c:
        n = n.strip('\n')
        hosts.append(n)
    for k in list(set(hosts)):
        for port in range(23454,23456):
            t=threading.Thread(target=get_ip_status,args=(k,port))
            t.start()
            threads.append(t)
    for t in threads:
            t.join()

def dojob():
    scheduler=BlockingScheduler()
    scheduler.add_job(check_port, 'interval',minutes=60,id='check_port')
    scheduler.start()

if __name__ == '__main__':
    dojob()


