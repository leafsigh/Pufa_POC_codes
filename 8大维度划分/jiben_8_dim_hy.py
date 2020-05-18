#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: heyue
"""

data = jiben
idd=data['id']
d1 = data.loc[:,['var_jb_44','var_jb_23','var_jb_95']]
d2 = data.loc[:,['var_jb_56','var_jb_92']]
d3 = data.loc[:,['var_jb_66','var_jb_67','var_jb_68']]
d4 = data.loc[:,['var_jb_6','var_jb_21','var_jb_24']]
d5 = data.loc[:,['var_jb_22','var_jb_26','var_jb_28','var_jb_34','var_jb_64','var_jb_65','var_jb_70','var_jb_37','var_jb_38','var_jb_71']]
d6 = data.loc[:,['var_jb_96','var_jb_64','var_jb_25','var_jb_29','var_jb_32','var_jb_33','var_jb_69','var_jb_72']]
d8 = data.loc[:, ['var_jb_89','var_jb_90','var_jb_88','var_jb_91']]


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

d11= I_F(d1)
d12= I_F(d2)
d13= I_F(d3)
d14=I_F(d4)
d15= I_F(d5)
d16= I_F(d6) 
d18= I_F(d8)  



hy=pd.concat([idd,d11,d12,d13,d14,d15,d16,d18],axis=1)
feature_names=['id','人行征信数据','商业征信信息','违法犯罪信息','存款信息','贷款信息','卡账户信息','金融资产信息']
hy.columns=feature_names
