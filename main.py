import streamlit as st
import pandas as pd
import datetime
import re
import csv

st.title('クリーンルーム予約')
st.write('荒木研　＠機械工学2号棟　309a室')
st.subheader('現在の予約状況')
#expander=st.expander('CSVの書式')
#expander.write('① CSV形式のみ対応')
#expander.write('② インデックス無し，1行目がカラムになります．')
#expander.write('③ 右下のダウンロードボタンでテンプレをダウンロードできます．')



KEY = st.secrets.AzureApiKey.key


st.write(KEY)
