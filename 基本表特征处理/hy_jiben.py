#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: hey
"""

import pandas as pd
import numpy as np
import seaborn as sns

data=pd.read_csv('~/Desktop/refer/jiben_origin.csv',low_memory=False)
#1. outlier
def newf(i):
    x=data.iloc[:,i]
    x.fillna(0,inplace=True)
    orix=round(np.log(x+1),2)
    a=x.copy()
    per=np.percentile(x,95)
    a[a<per]=0
    a[a>=per]=1
    w=pd.concat([orix,a],axis=1) 
    w.columns=[x.name, x.name+str('_outlier')]
    return w

# 2.negative value
def newnegf(nx):
    x=nx.copy()
    x.fillna(0,inplace=True)
    b=x.copy()
    b[b>0]=0
    b[b<0]=1
    xx=x.copy()
    xx[xx<0]=0
    orix=round(np.log(xx+1),2)
    a=x.copy()
    per=np.percentile(a,95)
    a[a<per]=0
    a[a>=per]=1
    w=pd.concat([orix,b,a],axis=1) 
    w.columns=['var_jb_64','var_jb_64'+str('_neg'),'var_jb_64'+str('_outlier')]
    return w
# check ratio between G and B
def e(di):
    t = pd.crosstab(di,data.iloc[:,0])
    p = t.iloc[:,0]/t.sum(axis=1)
    q = pd.concat([t,p],axis=1)
    return q

dii=data.iloc[:,].fillna('NA')
dii.value_counts()
e(dii)

#根据e(dii)的结果调整，连续变量要检查异常值和负数
newf(dii) #生成outlier
newnegf(dii)#生成negative count


## 3. Encoding
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
w=list(dii)
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(list(w))
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(w), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
qw=pd.DataFrame(onehot_encoded)
qw.iloc[:,0].value_counts()
qw.iloc[:,1].value_counts()
qw=pd.DataFrame(onehot_encoded,columns = ['var_jb_62_N','var_jb_62_NA','var_jb_62_Y'])
qw.head()

