# -*- coding: UTF-8 -*-
import requests
import  json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
filter_names =['ex_walletd.chain_SGY_wallet_rpc','ex_walletd.chain_UCN_wallet_rpc','ex_walletd.chain_KOIN_wallet_rpc','ex_walletd.chain_XRP_wallet_rpc','ex_walletd.chain_EOS_wallet_rpc','ex_walletd.chain_NULS_wallet_rpc','ex_walletd.chain_XLM_wallet_rpc']

headers = {'Content-Type': 'application/json'}
data ={'username':'xtcooperation@btc088.com','password':'xtnanjing123456'}
url = 'http://120.24.213.152:8380/exwalletd_admin'

sender = 'njbmkj0901@126.com'
reciver =['13770928380@126.com','peiqingfeng@btc088.com','yanghao@btc088.com']
last_names = []

def send_alarms(content,subject,name):
    name = json.dumps(name)
    content = content + name
    message  = MIMEText(content,'plain','utf-8')
    message['From'] = sender
    message['To'] ='13770928380@126.com'
    message['Subject'] = Header(subject,'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login(sender, 'MLTXLIIPAKWFYGXS')
    smtp.sendmail(sender, reciver, message.as_string())
    smtp.close()



def login():
    ret = requests.post(url + '/auth/login_jwt', json=data, headers=headers)
    if ret.status_code != 200 :
        return
    response = json.loads(ret.content.decode())
    return (response.get('result'))


def check_service_status():
    requestParamsMap={'page':1,'pageSize':1000}
    ret = requests.post(url+'/service_status/list',json= requestParamsMap,headers=headers)
    if ret.status_code != 200 :
        return
    response = json.loads(ret.content.decode())
    datas = ( response.get('result').get('data') )
    names = []
    for data in  datas :
        name = data.get('name')
        if data.get('online') != 1 and filter_names.count(name) == 0:
            names.append(name)
    warning =[]
    recover = list(last_names)
    last_names.clear()
    print ("recover is "+ ('').join(recover))
    for name in names :
        if recover.count(name) == 0:
            warning.append(name)
        else:
            recover.remove(name)
        last_names.append(name)    

    if len(recover) > 0 :
        print ("xt服务状态恢复："+('').join(recover))
        send_alarms("xt服务状态恢复：","xt 预警恢复邮件",recover)
    if len(warning) > 0:
        print('xt 服务状态预警:'+('').join(warning))
        send_alarms("xt服务状态预警: ", "xt 预警",warning)

def check_summary_status():
    requestParamsMap = {'page': 1, 'pageSize': 1000}
    ret = requests.post(url + '/coin_summary/list', json=requestParamsMap, headers=headers)
    if ret.status_code != 200:
        return
    print (ret.content)

if __name__ == '__main__':
    authToken = login()
    headers['Authorization'] =  'Bearer ' + authToken
    check_service_status()
    while True :
        try:
            time.sleep(600)
            check_service_status()
        except KeyboardInterrupt:
            exit(1)
        except:
            print("收到异常，继续监控")




