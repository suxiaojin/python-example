对配置文件进行增、删、改、查


#1.读取 ini配置文件 config.ini
[csdn.net]
user=suxiaojin
[51cto]
passwd=7150231

from configparser import ConfigParser
cfg=ConfigParser()
cfg.read('config.ini')
cfg.sections() ----['csdn.net','51cto']
cfg.get('csdn.net','user')    ---suxiaojin
改
cfg.set('csdn.net','user','sulingjun')
增：
cfg.add_section('test') ---增加节段
cfg.set('test','city','sz')

删：
cfg.remove_section('test')  --删除section
cfg.remove_option('test','city') --删除一个配置项


#2，读取json
with open('abc.json','r') as f:
    load_res=json.load(f)

#3.yaml
yaml.load