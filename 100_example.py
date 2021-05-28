'''
递归搜索目录最大的文件
sorted 可以对所有可迭代的对象进行排序操作
for root,dirs,files in os.walk(/root/python)
root ---代表当前目录
dirs  ---代表当前目录下的子目录
files ---代表当前目录下的文件
'''

import os

search_dir=/opt/python
result_files=[]
for root,dirs,files in os.walk(search_dir):
    for file in files:
        if file.endswith('.txt'):
            file_path=f'{root}/{file}'
            result_files.append(file_path,os.path.getsize(file_path)/1000)

print(sorted(result_files,key=lambda x:x[1],reverse=True)[:10])   #返回前10


'''
统计最高最低平均

语文 学号(101) 姓名 成绩
语文,101,suxiaojin,99,
'''
course_grades={}
with open('成绩.txt') as fin:
    for line in fin:
        line=line[:-1]
        course,sno,sname,grade =line.split(',')
        if course not in course_grades:
            course_grades[course]=[]
        course_grades[course].append(int(grade))

print(course_grades)
for course,grades in course_grades.items():
    print(course,max(grades),min(grades),sum(grades)/len(grades))


'''
实现不同文件的数据关联
'''
course_teacher_map={}
with open('a.txt') as fin:
    for line in fin:
        line=line[:-1]
        course,teacher=line.split(',')
        course_teacher_map[course]=teacher
print(course_teacher_map)

with open('b.txt') as fin:
    for line in fin:
        line=line[:-1]
        course,sno,sname,sgrade=line.split(',')
        teacher=course_teacher_map.get(course)
        print(course,teacher,sno,sname,sgrade)
