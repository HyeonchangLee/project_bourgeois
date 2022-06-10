import pandas as pd


# df_1= pd.read_excel('점포_2019년_z.xlsx')
# df_2= pd.read_excel('점포_2020년_z.xlsx')
# df_3= pd.read_excel('점포_2021년_z.xlsx')

# df_4= pd.concat([df_1,df_2,df_3])
# df_4.to_excel('점포_z.xlsx',index=False)


df_1= pd.read_excel('추정매출_2019년.xlsx')
df_2= pd.read_excel('추정매출_2020년.xlsx')
df_3= pd.read_excel('추정매출_2021년.xlsx')

df_4= pd.concat([df_1,df_2,df_3])
df_4.to_excel('추정매출.xlsx',index=False)