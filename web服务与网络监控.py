import time
from apscheduler.schedulers.blocking import BlockingScheduler
from urllib import request
from s_mail import SendEMail

def get_status(url):
    try:
        req=request.urlopen(url)
        return req.code
    except:
        return -1

def check_url():
    urls=['https://whitecoin.info/','https://explorer.whitecoin.info/','https://xwc.com/','https://bz.pandavedio.com/','https://tokenswap.info/#/']
    for url in urls:
        times=time.strftime('%Y-%y-%d %H:%M:%S',time.localtime())
        code=get_status(url)
        if code == 200:
            print('time:%s url:%s code=%d OK' %(times,url,code))
        else:
            print('time:%s url:%s code=%d ERROR' %(times,url,code))
            sm = SendEMail()
            sm.sendmail(['suxiaojin928380@126.com'], '域名出现问题', '域名%s访问不通' %url)


def dojob():
    scheduler=BlockingScheduler()
    scheduler.add_job(check_url, 'interval',minutes=10,id='check_url')
    scheduler.start()

if __name__ == '__main__':
    dojob()