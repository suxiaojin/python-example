'''
python的json标准库
json.dumps     将python对象编码成json字符串
json.loads        将json字符串解码为python对象


把数据转换为字典。然后通过json.dumps转换为json
'''

import json

dict_data={'name':'knight','city':'sz'}

str_data='{"name":"tom","city":"cs"}';

#字典转json
print(json.dumps(dict_data))
print(type(json.dumps(dict_data)))

#json字符串转字典
print(json.loads(str_data))
print(type(json.loads(str_data)))

'''
json数据：
    base_dirname   表示哪个文件夹（根目录）
    dirname 表示是base_dirname下的子文件夹
    child_dirs  表示它是dirname下面的子目录
    file表示是文件
'''
#1、先总体定义好我们需要的格式
path='/home/www/test'
def get_config_dir(path):
    res={'base_dirname':path,'child_dirs':[],'file':[]}

#2、遍历文件夹内的所有文件，以及目录结构以及子目录文件
#os.listdir: 可以把文件夹下的文件和文件夹展示出来（不包含子目录）
#os.path.isdir  可以判断它是不是目录

import json,os,sys

path=sys.argv[1]


def list_dir(path,res):
    for i in os.listdir(path):
        temp_dir=os.path.join(path,i)
        if os.path.isdir(temp_dir):
            temp={"dirname":i,'child_dirs':[],'files':[]}
            res['child_dirs'].append(list_dir(temp_dir,temp))
        else:
            res['files'].append(i)
    return res


def get_config_dirs(path):
    res={'base_dirname':path,'child_dirs':[],'file':[]}
    return list_dir(path,res)

if __name__=='__main__':
    print(json.dumps(get_config_dirs(path=path)))