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

df_2= pd.read_excel('생활인구.xlsx',usecols='B:D,F:P,W:AC')

a=df_2[(df_2['기준_년_코드']==2021) & (df_2['기준_분기_코드']==1)]
print(a)
x=[]
a['상권_코드']=a['상권_코드'].apply(areacode)
sn=a['상권_코드'].unique()


for i, val in enumerate (sn):
    b=a[a['상권_코드']==val]
    
    x_1=int(b['총_생활인구_수'].sum())
    x_2=int(b['남성_생활인구_수'].sum())
    x_3=int(b['여성_생활인구_수'].sum())
    x_4=int(b['연령대_10_생활인구_수'].sum())
    x_5=int(b['연령대_20_생활인구_수'].sum())
    x_6=int(b['연령대_30_생활인구_수'].sum())
    x_7=int(b['연령대_40_생활인구_수'].sum())
    x_8=int(b['연령대_50_생활인구_수'].sum())
    x_9=int(b['연령대_60_이상_생활인구_수'].sum())
    w_1=int(b['일요일_생활인구_수'].sum())
    w_2=int(b['월요일_생활인구_수'].sum())
    w_3=int(b['화요일_생활인구_수'].sum())
    w_4=int(b['수요일_생활인구_수'].sum())
    w_5=int(b['목요일_생활인구_수'].sum())
    w_6=int(b['금요일_생활인구_수'].sum())
    w_7=int(b['토요일_생활인구_수'].sum())
    f=[val,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,w_1,w_2,w_3,w_4,w_5,w_6,w_7]
    x.append(f)
p2=pd.DataFrame(x,columns=['지역','전체','남성','여성','10대','20대','30대','40대','50대','60대 이상','일','월','화','수','목','금','토'])
print(p2)
p2.to_excel('생활인구_21_01.xlsx')
