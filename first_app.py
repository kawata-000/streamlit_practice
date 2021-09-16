import streamlit as st
import time


st.title('Streamlit超入門')

#st.write('Display Image')

st.write('プログレスバーの表示')
'Start!!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+i}')
    bar.progress(i + 1)
    time.sleep(0.1)



left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示させます')
if button:
    right_column.write('ここから右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問合せ1の回答です')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答です')

text = st.text_input('あなたの趣味を教えてくださ')
condition = st.slider('あなたの今日の調子は?', 0, 100,50)



#'あなたの趣味は:', text
#'コンディション :' ,condition


#option = st.selectbox(
#    '貴方が好きな数字を教えてください、',
#    list(range(1,11))
#)

#'貴方の好きな数字は、',option,'です。'


#if st.checkbox('Show Image'):
#    img = Image.open('red.devils.jpeg')
#    st.image(img, caption='man_united',use_column_width=True)
#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#   columns= ['lat', 'lon']
#)

#st.map(df)

#st.table(df.style.highlight_max(axis=0))

#"""
# 1
## 2
### 3

#```python
#import pandas as pd
#import streamlit as st
#import numpy as np
#```

#"""



