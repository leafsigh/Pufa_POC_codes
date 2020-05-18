# -*- coding: utf-8 -*-
import os
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import OneHotEncoder

os.chdir('C:/Users/yangjy/Desktop/d')


data = pd.read_csv('jiben_vars_new_0429.csv')
data = data.loc[:,['id','var_jb_71','var_jb_72','var_jb_77','var_jb_78',
                   'var_jb_89','var_jb_90','var_jb_92','var_jb_93',
                   'var_jb_95','var_jb_96','var_jb_98','bad']]
train = data[(data.bad =='G')|(data.bad =='B')]

def e(di):
    t = pd.crosstab(di,train.loc[:,'bad'])
    p = t.iloc[:,0]/t.sum(axis=1)
    q = pd.concat([t,p],axis=1)
    return q
e(dii)

def f(di):
    t = pd.crosstab(di,train.loc[:,'bad'])
    p = t.iloc[:,0]/t.sum(axis=1)
    q = pd.concat([t,p],axis=1)
    return q

k = 71;di = train.loc[:,'var_jb_'+str(k)].fillna(0);di = di.astype(int);f(di)
di = np.log(di+1)


dii =  train.loc[:,'var_jb_'+str(k)].fillna(0)
dii[dii !=0] = 1
dii = np.log(dii+1)
dii = dii.astype(int)
dii.replace({'±\x0c1391565':0},inplace=True)

dii = dii.copy()
dii = dii.fillna(0)
dii = dii.values
dii = dii[:,[1]]
enc = OneHotEncoder(sparse=False)
dii = enc.fit_transform(dii)
dii = np.array(dii)
dii = pd.DataFrame(dii,columns = ['var_jb_71_0','var_jb_71_1','var_jb_71_2'])


p95 = np.percentile(di,95)
outlier = di.copy()
outlier[outlier<p95]=0
outlier[outlier>=p95]=1
outlier.name = 'var_jb_'+str(k)+'_outlier'

d = pd.DataFrame()
d = pd.concat([d,dii],axis=1)
d.to_csv('jiben_part_ 3.csv',index=False)


