import streamlit as st
def footer_home():
    st.markdown("""
    <div style="display:flex; flex-direction:column;gap:6px; align-items:center; justify-content:center; margin-bottom:30px;margin-top:30px">
         
    <p style="font-weight:bold;color:white;" >Created by Shreya Patwa</p>   
    </div>""",unsafe_allow_html=True)

def footer_dashboard():
    st.markdown("""
    <div style="display:flex; flex-direction:column;gap:6px; align-items:center; justify-content:center; margin-bottom:30px;margin-top:30px">
         
    <p style="font-weight:bold;color:black;" >Created by Shreya Patwa</p>   
    </div>""",unsafe_allow_html=True)