import streamlit as st
from PIL import Image
import time
st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
st.write('Start!!')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

st.write('Done!!')

left_column, right_column = st.columns(2)
if left_column.button('右カラムに文字を表示'):
    right_column.write('ここは右カラムです。')


expander = st.expander('問い合わせ')
expander.write('問い合わせ回答')

if st.checkbox('Show Image'):
    img = Image.open('LINE_ALBUM_人力車_220831_7.jpg')
    st.image(img,caption='Otaru', use_column_width=True)

option = st.sidebar.selectbox(
    '貴方が好きな数字を教えてください。',
    list(range(1, 11))

)

st.write(f'あなたが好きな数字は{option}です。')


text = st.text_input('あなたの趣味を教えてください。')
st.write(f'あなたの趣味：{text}')

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
st.write(f'コンディション：{condition}')

