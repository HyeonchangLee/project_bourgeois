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

year=[2019,2020,2021]

for i in year:
    df=pd.read_excel(f'점포_{i}년.xlsx',usecols='B:C,F:H,J:K,P')

    # 분기, 년도

    a=df.sort_values(['상권_코드','기준_년_코드','기준_분기_코드','서비스_업종_코드'],ascending=[True,True,True,True])
    a=df[(df['서비스_업종_코드']=='CS100001')|(df['서비스_업종_코드']=='CS100002')|(df['서비스_업종_코드']=='CS100003')|(df['서비스_업종_코드']=='CS100004')|(df['서비스_업종_코드']=='CS100005')|(df['서비스_업종_코드']=='CS100006')|(df['서비스_업종_코드']=='CS100007')|(df['서비스_업종_코드']=='CS100008')|(df['서비스_업종_코드']=='CS100009')|(df['서비스_업종_코드']=='CS100010')]
    a['상권_코드']=a['상권_코드'].apply(areacode)
    a.to_excel(f'점포_{i}년_z.xlsx',index=False)
