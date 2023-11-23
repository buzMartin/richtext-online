import streamlit as st
from PIL import Image


h1 = st.markdown('# 欢迎来到本地化playground!🎉')
image = Image.open('icon.png')

st.set_page_config(
    page_title='游戏本地化Playground',
    layout='wide',
    initial_sidebar_state='auto'
    )
c1, c2 = st.columns(2)
with c1:
    ori_area = st.text_area('输入语言表里的文本')
    param = st.text_input('参数')
with c2:
    new_area = st.text_area('实际显示效果')
    btn = st.button('显示')


# 在Streamlit应用中显示图片
col1,col2,col3 = st.columns([0.2,0.6,0.2])
with col2:
    st.image(image, caption='这是我的图片', use_column_width=False)
