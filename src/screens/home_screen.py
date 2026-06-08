import streamlit as st 
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home

def home_screen():

    header_home()
    style_background_home()
    style_base_layout()


    col1,col2=st.columns(2)

   
    with col1:
        st.header("I'm Student")
        st.image("https://static.vecteezy.com/system/resources/previews/020/274/235/original/student-icon-for-your-website-design-logo-app-ui-free-vector.jpg",width=100)
        if(st.button('Student Portal',type='primary',icon=':material/arrow_outward:',icon_position='right')):
            st.session_state['login_type']='student'
            st.rerun()
    with col2:
        st.header("I'm Teacher")
        st.image("https://tse1.mm.bing.net/th/id/OIP.RPGryXLukyz7T0xjK-SttAHaHa?pid=Api&P=0&h=180",width=100)
        if(st.button('Teacher Portal',type='primary',icon=':material/arrow_outward:',icon_position='right')):
            st.session_state['login_type']='teacher'
            st.rerun()
    footer_home()
