import pandas as pd
import csv
#from datetime import date
df=pd.read_csv('date.csv')
#date=pd.DataFrame({'Date':[0,1,2]})
dates_list=pd.date_range('2021-01-01',periods=7000)
dates=pd.DataFrame({'Date':dates_list})
#print(df)
#print(date)
df2=pd.concat([df,dates])
df2.iloc[:,1:]='-'
print(df2)

df2.to_csv('CR_date.csv')


