import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
from sympy import rotations
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

# '지역','전체','남성','여성','10대','20대','30대','40대','50대','60대 이상'
df_a=pd.read_excel('상주인구_21_01.xlsx')
df_b=pd.read_excel('직장인구_21_01.xlsx')
df_c=pd.read_excel('생활인구_21_01.xlsx')   # 생활인구\
df_d=pd.read_excel('추정매출_21_01.xlsx')
df_e=pd.read_excel('소득소비_21_01.xlsx')



x=np.arange(25)
# plt.bar(x-0.3,df_b['전체'],label='직장',width=0.2)
# plt.bar(x-0.1,df_c['전체']/100,label='생활',width=0.2)
# plt.bar(x+0.1,df_a['전체'],label='상주',width=0.2)
# # plt.bar(x+0.3,df_d['전체'],label='전체매출',width=0.2)
# plt.legend(loc='upper left')
# plt.title('남녀 직장, 상주인구 그래프')
# plt.xlabel('지역구',loc='right')
# plt.ylabel('인구',loc='top')
# plt.xticks(x,df_a['지역'],size=8,rotation=90)





# y=df_a['남성']
# z=df_a['여성']
# y_1=df_b['남성']
# z_1=df_b['여성']
# y_2=df_c['남성']
# z_2=df_c['여성']
# alle=df_c['전체']
# mm=df_d['남성']
# ww=df_d['여성']
# eat=df_e['전체']

# # plt.bar(x-0.25,mm,label='남성매출',width=0.25)
# plt.bar(x,df_d['전체'],label='전체매출',width=0.25)
# # plt.bar(x+0.25,ww,label='여성매출',width=0.25)
# # plt.plot(x,y_2,label='생활남성',color='red')
# # plt.plot(x,z_2,label='생활여성',color='blue')
# plt.legend(loc='upper left')
# plt.title('남녀인구별 매출 그래프')
# plt.xlabel('지역구',loc='right')
# plt.ylabel('인구',loc='top')
# plt.xticks(x,df_a['지역'],size=8,rotation=90)


# plt.figure()
# # plt.bar(x,df_b['전체'],label='직장인구',width=0.25)
# plt.bar(x-0.3,y_1,label='직장남성',width=0.2)
# plt.bar(x-0.1,z_1,label='직장여성',width=0.2)
# plt.bar(x+0.1,y,label='상주남성',width=0.2)
# plt.bar(x+0.3,z,label='상주여성',width=0.2)
# plt.legend(loc='upper left')
# plt.title('남녀 직장, 상주인구 그래프')
# plt.xlabel('지역구',loc='right')
# plt.ylabel('인구',loc='top')
# plt.xticks(x,df_a['지역'],size=8,rotation=90)

# plt.figure()
# plt.bar(x-0.2,y_2,label='생활남성',width=0.2)
# plt.bar(x,z_2,label='생활여성',width=0.2)
# plt.bar(x+0.2,alle,label='생활전체',width=0.2)

# plt.legend(loc='upper left')
# plt.title('남녀생활인구 그래프')
# plt.xlabel('지역구',loc='right')
# plt.ylabel('인구',loc='top')
# plt.xticks(x,df_a['지역'],size=8,rotation=90)

# plt.figure()
# plt.bar(x,alle,label='생활전체',width=0.25)
# plt.plot(x,df_c['10대']/df_c['전체']*100,label='10대')
# plt.plot(x,df_c['20대']/df_c['전체']*100,label='20대')
# plt.plot(x,df_c['30대']/df_c['전체']*100,label='30대')
# plt.plot(x,df_c['40대']/df_c['전체']*100,label='40대')
# plt.plot(x,df_c['50대']/df_c['전체']*100,label='50대')
# plt.plot(x,df_c['60대 이상']/df_c['전체']*100,label='60대 이상')
# plt.legend(loc='upper left')
# plt.title('연령대별 생활인구 그래프')
# plt.xlabel('지역구',loc='right')
# plt.ylabel('인구',loc='top')
# plt.xticks(x,df_a['지역'],size=8,rotation=90)


plt.show()