import streamlit as st
import pandas as pd
import datetime
import re
import csv

st.title('研究紹介')


pass_true=st.secrets["password"]
pass_in = st.text_input('PASSWORD')
pass_st=0

if pass_in==pass_true:
  st.write("OK")
  pass_st=1
elif pass_in=='':
  st.write("パスワードを入力し、Enterキーを押してください")
else:
  st.write("パスワードが違います")

if pass_st==1:
  st.write('荒木研　＠機械工学2号棟　309a室')
  st.subheader('現在の予約状況')

