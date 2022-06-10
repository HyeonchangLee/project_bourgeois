import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
from sympy import rotations
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10


df=pd.read_excel('직장인구_21_01.xlsx')

z=input('검색할 지역을 입력하세요.')

a=df.지역 ==z

b=int(df[a]['20대'])/int(df[a]['전체'])*100
c=int(df[a]['30대'])/int(df[a]['전체'])*100
d=int(df[a]['40대'])/int(df[a]['전체'])*100
e=int(df[a]['50대'])/int(df[a]['전체'])*100
f=int(df[a]['60대 이상'])/int(df[a]['전체'])*100
x=['20대','30대','40대','50대','60대 이상']
y=[b,c,d,e,f]
colors=['#5d84c7','#f788f0','#e9f5cb','#e4f5f3','#e01f26']
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}

plt.title(f'{z} 직장인구 연령대별 그래프')
plt.pie(y,labels=x, autopct='%.2f',colors=colors,wedgeprops=wedgeprops,pctdistance=0.7)
plt.show()