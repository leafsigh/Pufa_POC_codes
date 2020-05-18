# -*- coding: utf-8 -*-
import os
import pandas as pd

os.chdir('C:/Users/yangjy/Desktop/d')
data = pd.read_csv('kw_poc_card_20200424.csv')
dd = data.loc[:,['id','latest24state']]
dd.fillna('00',inplace=True)
del(data)

#将各个id的多条24期状态合成一个长条
def S(x):
    x1=''.join(list(x.iloc[:,1]))
    return x1

a = dd.groupby(dd['id']).apply(S)
a.to_csv('card_24_str.csv')
del(a)
b = pd.read_csv('card_24_str.csv')


#计算每个id合成的24期状态长条中各个字符出现的次数，得到一个字典
def C(message):
    count={}
    for character in message:
        count.setdefault(character,0)
        count[character]=count[character]+1
    return count

c1 = b.iloc[:,1].apply(C)
r1 = pd.concat([b,c1],axis=1)
r1.columns=['id','total_str','dic_str']
r1.to_csv('card_24_str.csv',index=False)
del(b)


#计算整个数据中24期状态所有可能的取值
def D(d):
    dd = set(d.keys())
    return dd
c2 = r1.iloc[:,2].apply(D)

c3 = set()
for i in range(len(c2.values)):
    c3 = c3|c2.values[i]
   
#c3 = ['0','1','#','*','/','2','3','4','5','6','7','C','G','N']
#c3 = set(c3)


#将各个id的24期状态中没有在C3中出现的key也加进去，value填0
def E(e):
    e1 = c3 - set(e.keys())
    e1 = list(e1)
    for j in range(len(e1)):
        e[e1[j]] = 0
    return e
g1 = r1.iloc[:,2].apply(E)


#将各个id的24期状态的字典按key排序，输出
def G(g):
    f = zip(g.keys(), g.values())
    c = sorted(f)
    return c
g2 = g1.apply(G)

g2 = pd.concat([r1.loc[:,'id'],g2],axis=1)
g2.to_csv('card_24_derive.csv',index=False)
#将输出的结果在Excel中按":"分组





