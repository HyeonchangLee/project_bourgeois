import pandas as pd
import numpy as np
def areacode(a):
    if a<=2110037 or a==2110531:
        return '종로구'
    elif a<=2110057 or a==2110591:
        return '중구'
    elif a==2210221:
        return '성북구'
    elif a<=2110099 :
        return '용산구'
    elif a<=2110138 :
        return '성동구'
    elif a<=2110180 :
        return '광진구'
    elif a<=2110232 :
        return '동대문구'
    elif a<=2110279 :
        return '중량구'
    elif a<=2110336:
        return '성북구'
    elif a<=2110381 :
        return '강북구'
    elif a<=2110413 :
        return '도봉구'
    elif a<=2110442 :
        return '노원구'
    elif a<=2110492 :
        return '은평구'
    elif a<=2110539 :
        return '서대문구'
    elif a<=2110590 :
        return '마포구'
    elif a<=2110628 :
        return '양천구'
    elif a<=2110679 :
        return '강서구'
    elif a<=2110722 :
        return '구로구'
    elif a<=2110755 :
        return '금천구'
    elif a<=2110817 :
        return '영등포구'
    elif a<=2110852 :
        return '동작구'
    elif a<=2110902 :
        return '관악구'
    elif a<=2110948 :
        return '서초구'
    elif a<=2111002 :
        return '강남구'
    elif a<=2111047 :
        return '송파구'
    elif a<=2111090 :
        return '강동구'

df=pd.read_excel('추정매출.xlsx',usecols='B:D,F:H,J,AI:AJ,AX:BE')
df['상권_코드']=df['상권_코드'].apply(areacode)

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

                x_1=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'분기당_매출_금액'}])
                x_2=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'주중_매출_금액'}])
                x_3=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'주말_매출_금액'}])
                x_4=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'남성_매출_금액'}])
                x_5=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'여성_매출_금액'}])
                x_6=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'연령대_10_매출_금액'}])
                x_7=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'연령대_20_매출_금액'}])
                x_8=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'연령대_30_매출_금액'}])
                x_9=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'연령대_40_매출_금액'}])
                x_10=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'연령대_50_매출_금액'}])
                x_11=int(a.groupby(['상권_코드','서비스_업종_코드']).get_group((i,j)).sum()[{'연령대_60_이상_매출_금액'}])
   
                h=[aa,bb,i,j,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10,x_11]



                z.append(h)
aaa=pd.DataFrame(z,columns=['년도','분기','지역','서비스_업종_코드','전체','주중','주말','남성','여성','10대','20대','30대','40대','50대','60대 이상'])
print(aaa)
aaa.to_excel('추정매출_zz.xlsx',index=False)
