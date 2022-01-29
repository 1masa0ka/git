import streamlit as st
import pandas as pd
import datetime
import re
import csv
import zipfile
import io
from PIL import Image

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
  filename = "./DATA.zip"
  with zipfile.ZipFile(filename, "r") as zp:
    for info in zp.infolist():
        # 「zipファイル名/」については処理をしない    
      with zp.open(info.filename,pwd=pass_in.encode("utf-8")) as img_file:
        # 画像のバイナリデータを読み込む
        img_bin = io.BytesIO(img_file.read())
        # バイナリデータをpillowから開く
        st.image(img_bin, caption='Sunrise by the mountains')
    #zp.extractall(pwd=pass_in.encode("utf-8"))
    st.write("The extract is complete.")
        
  st.sidebar.write('テーマ選択')
  
  

  
