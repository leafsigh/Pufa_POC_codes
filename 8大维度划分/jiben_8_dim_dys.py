# -*- coding: utf-8 -*-
import os
import pandas as pd

os.chdir('C:/Users/yangjy/Desktop/d')
data= pd.read_csv('jiben_vars_new.csv')

def I_F(data):
    d = data.isnull()
    if len(list(d.shape))>1:
        d.replace({True:1,False:0},inplace=True)
        d = d.sum(axis=1)
        d = d>0
        d.replace({True:1,False:0},inplace=True)
    else:
        d.replace({True:1,False:0},inplace=True)
    return d

d1 = data.loc[:,['var_jb_41','var_jb_1','var_jb_7','var_jb_11','var_jb_5','var_jb_8',
                 'var_jb_19','var_jb_27','var_jb_35','var_jb_43','var_jb_97']]
d2 = data.loc[:,['var_jb_4','var_jb_48','var_jb_45','var_jb_46','var_jb_47','var_jb_49',
                 'var_jb_50','var_jb_51','var_jb_52','var_jb_53','var_jb_54','var_jb_55']]
d3 = data.loc[:,['var_jb_18','var_jb_14','var_jb_85','var_jb_12','var_jb_13']]
d4 = data.loc[:,['var_jb_60','var_jb_76']]
d5 = data.loc[:,['var_jb_62','var_jb_3','var_jb_10','var_jb_36']]
d6 = data.loc[:,['var_jb_73','var_jb_57','var_jb_74','var_jb_75','var_jb_84']]
d7 = data.loc[:,'var_jb_63']
d8 = data.loc[:,'var_jb_61']
d9 = data.loc[:,'var_jb_59']

r1 = I_F(d1)
r2 = I_F(d2)
r3 = I_F(d3)
r4 = I_F(d4)
r5 = I_F(d5)
r6 = I_F(d6)
r7 = I_F(d7)
r8 = I_F(d8)
r9 = I_F(d9)
r = pd.concat([data.loc[:,'id'],r1,r2,r3,r4,r5,r6,r7,r8,r9],axis=1)
r.columns = ['id','基本信息','教育信息','职业信息','单位信息','地址信息',
             '联系方式','多家庭电话','多单位电话','多联系人电话']
r.to_csv('binary.csv',index=False)



data = pd.read_csv('outsidedata_0429.csv')
d1 = pd.read_csv('kw_poc_loan_20200424.csv')
d2 = pd.read_csv('kw_poc_card_20200424.csv')

d3 = data.id.isin(d1.loc[:,'id'])
d3.replace({True:1,False:0},inplace=True)
d3.name = 'if_loan'

d4 = data.id.isin(d2.loc[:,'id'])
d4.replace({True:1,False:0},inplace=True)
d4.name = 'if_card'

data = pd.concat([data,d3],axis=1)
data = pd.concat([data,d4],axis=1)
data.to_csv('binary.csv',index=False)

