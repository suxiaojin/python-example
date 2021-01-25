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