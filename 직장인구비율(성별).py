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
a_1=int(df[a]['남성'])/int(df[a]['전체'])*100
b=int(df[a]['여성'])/int(df[a]['전체'])*100

x=['남성','여성']
y=[a_1,b]
colors=['#22ABD6','#E63426']
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}

plt.title(f'{z} 직장인구 성별 비율')
plt.pie(y,labels=x, autopct='%.2f',colors=colors,wedgeprops=wedgeprops,pctdistance=0.7)
plt.show()