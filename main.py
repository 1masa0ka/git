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
pass_true2=st.secrets["password2"]
pass_st=0
pass_in = st.text_input('PASSWORD')

if pass_st==0:
  if pass_in==pass_true or pass_in==pass_true2:
    #st.write("OK")
    pass_st=1
  elif pass_in=='':
    st.write("パスワードを入力し、Enterキーを押してください")
  else:
    st.write("パスワードが違います")

if pass_st==1:
  st.sidebar.write('表示')
  slides_1 = st.sidebar.radio("テーマ",('1. 微細構造表面における凝縮水滴の凍結観察', '2. 機械学習を用いたPEFC触媒層の乾燥プロセス開発','3. 畳み込みニューラルネットワークを用いた気泡認識'))
  if str(slides_1[0])==str(1):
    slides_2 = st.sidebar.radio("スライド番号",('1. 背景・目的', '2. 背景・目的', '3. 実験方法(試料表面)','4. 実験方法(観察装置)',
                                          '5. 結果(観察)','6. 結果(成長分析)','7. 考察(仮説)','8. 考察(先行研究)','9. 考察(本研究)'))
  elif str(slides_1[0])==str(2):
    slides_2 = st.sidebar.radio("スライド番号",('1. 背景・目的', '2. 背景・目的', '3. 実験方法（操作）','4. 実験方法（センサ）','5. 実験結果','6. 考察'))
  
  else:
    slides_2 = st.sidebar.radio("スライド番号",('1. 背景・目的', '2. 疑似気泡画像合成アルゴリズム', '3. 気泡認識①','4. 気泡認識②','5. CNNアーキテクチャの構造','6．結果','7．結果','8．まとめ・今後の課題','9．動画(追記)'))
  
  filename = "./DATA.zip"
  view_name='DATA/'+str(str(slides_1[0]))+str(str(slides_2[0]))
  
  with zipfile.ZipFile(filename, "r") as zp:
    #画像表示
    if view_name!='DATA/39':
      with zp.open(view_name+'.JPG',pwd=pass_true.encode("utf-8")) as img_file:
        img_bin = io.BytesIO(img_file.read())
        img = Image.open(img_bin)
        st.image(img)
    #動画表示
    else:
      video_file = open('bubble.mp4', 'rb')
      video_bytes = video_file.read()
      st.video('bubble.mp4') 

    #テキスト表示
    with zp.open(view_name+'.txt',pwd=pass_true.encode("utf-8")) as txt_file:
      txtdata = txt_file.read().decode('utf_8')
      #st.write(txtdata)
      txt_s=txtdata.split('\n')
      for i in range(len(txt_s)):
        st.write(txt_s[i])
      
      
      
