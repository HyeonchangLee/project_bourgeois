import pandas as pd

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

# df=pd.read_excel('상권소득소비.xlsx',usecols='B:C,F:G,J:K')
df_2= pd.read_excel('추정매출.xlsx',usecols='B:D,F:G,J,AI:AJ,AX:BE')
x=[]
z=[]
y=[]
# 분기, 년도
year=[2019,2020,2021]
bungi=[1,2,3,4]
for i in year:
    for j in bungi:
        # a=df[(df['기준_년_코드']==i) & (df['기준_분기_코드']==j)]
        # a=a.sort_values('상권_코드',ascending=True)
        # a['상권_코드']=a['상권_코드'].apply(areacode)

        # for key, val in enumerate (sn):
        #     b=a[a['상권_코드']==val]
            
        #     x_1=int(b['지출_총금액'].sum())
        #     x_2=int(b['식료품_지출_총금액'].sum())

        #     f=[i,j,val,x_1,x_2]
        #     x.append(f)


        a=df_2[(df_2['기준_년_코드']==i) & (df_2['기준_분기_코드']==j)]
        a=a.sort_values('상권_코드',ascending=True)
        a['상권_코드']=a['상권_코드'].apply(areacode)

        sn=a['상권_코드'].unique()
        for key, val in enumerate (sn):
            b=a[a['상권_코드']==val]
            
            x_1=int(b['분기당_매출_금액'].sum())
            x_2=int(b['주중_매출_금액'].sum())
            x_3=int(b['주말_매출_금액'].sum())
            x_4=int(b['남성_매출_금액'].sum())
            x_5=int(b['여성_매출_금액'].sum())
            x_6=int(b['연령대_10_매출_금액'].sum())
            x_7=int(b['연령대_20_매출_금액'].sum())
            x_8=int(b['연령대_30_매출_금액'].sum())
            x_9=int(b['연령대_40_매출_금액'].sum())
            x_10=int(b['연령대_50_매출_금액'].sum())
            x_11=int(b['연령대_60_이상_매출_금액'].sum())

            f=[i,j,val,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10,x_11]
            y.append(f)
# p1=pd.DataFrame(x,columns=['년도','분기','지역','전체','식료품'])
p2=pd.DataFrame(y,columns=['년도','분기','지역','전체','주중','주말','남성','여성','10대','20대','30대','40대','50대','60대 이상'])


# p1 소득소비 p2 추정매출
# print(p1)
print('-'*30)
print(p2)
print('-'*30)

# p1.to_excel('소득소비_z.xlsx')
p2.to_excel('추정매출_z.xlsx')