import streamlit as st
import pandas as pd
import datetime
import re
import csv

st.title('クリーンルーム予約')
st.write('荒木研　＠機械工学2号棟　309a室')
st.subheader('現在の予約状況')

pass_true=st.secrets["password"]
pass_in = st.text_input('PASSWORD')

if pass_in==pass_true:
  st.write("OK")
else:
  st.write("パスワードが違います")


