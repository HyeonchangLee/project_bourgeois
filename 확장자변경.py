import pandas as pd

a=pd.read_csv('추정매출_2019년.csv',encoding='cp949')

a.to_excel('추정매출_2019년.xlsx')