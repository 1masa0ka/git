import pandas as pd
import csv

df=pd.read_csv('CR_date.csv',header=None)
df.iloc[0,0]='Date'
df.to_csv('CR_date2.csv', header=False, index=False,encoding='utf_8_sig')