# -*- coding: utf-8 -*-
__author__ = 'suxiaojin'
__date__ = '2021/1/26 0026 上午 0:13'
#数字组合
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)

#  个税计算
profit=int(input('show me the money:'))
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)

#这是第几天
def isleapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))
Dofm=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input('Year:'))
month=int(input('month:'))
day=int(input('day:'))
if isleapYear(year):
    Dofm[2]+=1
    for i in range(month):
        res+=Dofm[i]
    print(res+day)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld ' % (i, j, i * j), end='')
    print()

#1-100之和
res=0
for i in range(1,101):
    res+=i
print(res)

#遍历列表

l=['moyu','niupi','xuecaibichi','shengfaji','42']
for i in range(len(l)):
    print(l[i])

#查找字典最大值
person = {"li":91,"wang":50,"zhang":20,"sun":22,'su':90}
m = 'li'
for key in person.keys():
    if person[m] < person[key]:
        m = key
print ('%s,%d' % (m,person[m]))

#列表中求偶数的和
a=[1,2,3,4,5,6]
s=sum([num for num in a if num%2==0])
print(s)

#列表中删除元素
a=[1,2,3,4,5]
del a[1::2]
print(a)

#用空格分隔的整数到一个列表
l=list(map(int,input().split()))
print(l)

#记数，某个值出现的次数
import re
print(len(re.findall('python','python is a programing language.python is python')))

#序列解包
s={'name':'sxj','age':18,'job':'manage'}
a,b,c=s
print(a,b,c)
a,b,c=s.items()
print(b)
k,v,a=s.values()
print(a)