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
  #st.write("OK")
  pass_st=1
elif pass_in=='':
  st.write("パスワードを入力し、Enterキーを押してください")
else:
  st.write("パスワードが違います")

if pass_st==1:
  st.sidebar.write('テーマ選択')
  slides_1 = st.sidebar.radio("テーマ選択",('1. abc', '2. def'))
  
  slides_2 = st.radio("スライド番号",('1. abc', '2. def', '3. efg','4. aop','5. tet'))
  filename = "./DATA.zip"
  view_name='DATA/'+str(str(slides_1[0]))+str(str(slides_2[0]))
  
  with zipfile.ZipFile(filename, "r") as zp:
    #画像表示
    with zp.open(view_name+'.png',pwd=pass_in.encode("utf-8")) as img_file:
      img_bin = io.BytesIO(img_file.read())
      img = Image.open(img_bin)
      st.image(img, caption='Sunrise by the mountains')
    #テキスト表示
    with zp.open(view_name+'.txt',pwd=pass_in.encode("utf-8")) as txt_file:
      txtdata = txt_file.read().decode('utf_8')
      st.write(txtdata)
      
  #zp.extractall(pwd=pass_in.encode("utf-8"))
  st.write("The extract is complete.")
        
  

  
