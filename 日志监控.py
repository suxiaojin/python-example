'''
方法一：通过命令行，读取文件

'''

from s_mail import SendEMail
import subprocess

logfile='pay-api_error.log'
cmd='tail -1 {0}'.format(logfile)
key_word='wechat'

pp=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
while True:
    line=pp.stdout.readline().strip()
    line=line.decode()
    if key_word in line:
        print('有关键字{0},发送告警'.format(key_word))
        sm=SendEMail()
        sm.sendmail(['suxiaojin928380@126.com'],'主题','测试')



'''
第三方方库  pyinotify
'''
import pyinotify
import time,os
from s_mail import SendEMail

key_word='wechat'

class ProcessTransientFile(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self,event):
        line=file.readline()
        if key_word in line:
            print('有关键字{0},发送告警'.format(key_word))
            sm = SendEMail()
            sm.sendmail(['suxiaojin928380@126.com'], '主题', '测试')

filename='/tmpp/pay-api_error.log'
file=open(filename,'r')

st_results=os.stat(filename)
st_size=st_results[6]
file.seek(st_size)

wm=pyinotify.WatchManager()
notifier=pyinotify.Notifier(wm)
wm.watch_transient_file(filename,pyinotify.IN_MODIFY,ProcessTransientFile)
notifier.loop()




