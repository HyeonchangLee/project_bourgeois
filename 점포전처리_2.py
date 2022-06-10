import pandas as pd
import numpy as np


df=pd.read_excel('점포_z.xlsx')


# print(df)
year=[2019,2020,2021]
bungi=[1,2,3,4]

sg=df['상권_코드'].unique()
y=['CS100001','CS100002','CS100003','CS100004','CS100005','CS100006','CS100007','CS100008','CS100009','CS100010']
z=[]
for aa in year:
    for bb in bungi:
        a=df[(df['기준_년_코드']==aa) & (df['기준_분기_코드']==bb)]
        for i in sg:
            for j in y:

                x_1=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'점포_수'}])
                x_2=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'유사_업종_점포_수'}])
                x_3=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'프랜차이즈_점포_수'}])
                h=[aa,bb,i,j,x_1,x_2,x_3]



                z.append(h)
aaa=pd.DataFrame(z,columns=['년도','분기','지역','서비스_업종_코드','점포','유사','프렌차이즈'])
print(aaa)
aaa.to_excel('점포_zz.xlsx',index=False)